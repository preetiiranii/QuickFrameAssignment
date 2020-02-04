import csv,re
import sys,os

sys.path.append(os.getcwd())

import DBUtil, Pipeline

data_file = os.getcwd() + r"\DataEngineerDataSet.csv"
running_total_dict = {}
EMDASH = '—'

def run_pipeline():

    with open(data_file, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_num = 0
        insert_columns = None

        for row in csv_reader:

            if line_num == 0:

                setup_tables(row) # Create both table here with column names with headers available in 0th row
                line_num += 1
            else:
                print(row)
                cleaned_row = Pipeline.data_cleanup(row) # Step 1: data cleanup for first column

                if cleaned_row is not None:  # Step 2: Normalize the date column


                    #print(cleaned_row[21].split('-'))
                    cleaned_row[21] = re.sub(EMDASH, '-', cleaned_row[21])
                    normalized_row = Pipeline.normalize_row(cleaned_row)
                    #insert_stmt = "INSERT INTO data_normalized(" + insert_columns + ") VALUES (" + '"{0}"'.format('", "'.join(normalized_row)) + "\"0\", \"0\")"

                    #print(insert_stmt)
                    #DBUtil.insert_table(insert_stmt)
                    #DBUtil.select_table("data_normalized")

                    normalized_row = cleaned_row
                    Pipeline.running_total(normalized_row, running_total_dict) # Step 3: Calculate running_total

                line_num += 1
                if line_num == 20:
                    break;

        #print(running_total_dict)

        # Populate classification_totals table with calculated running totals
        for classification, totals in running_total_dict.items():
            insert_stmt = "INSERT INTO classification_totals(Classification, Totals) VALUES (\"" + classification +"\",\""+ str(totals) +"\")"
            #print(insert_stmt)
            DBUtil.insert_table(insert_stmt)

        DBUtil.commit()
        #DBUtil.select_table("classification_totals")


def setup_tables(row):

    # Create query statement for data_normalized table with two additional columns
    tup = tuple(word.replace(" ", "_") for word in row)
    insert_columns = f'{", ".join(tup)}' + ', Object_Start_date' + ', Object_End_date'
    columns = f'{" VARCHAR(255), ".join(tup)}'
    create_stmt = "CREATE TABLE data_normalized (" + columns + \
                  " VARCHAR(255), Object_Start_date VARCHAR(255), Object_End_date VARCHAR(255))"

    # Create data_normalized table
    DBUtil.drop_table('data_normalized')
    DBUtil.create_table(create_stmt)

    # Create classification_totals table
    DBUtil.drop_table('classification_totals')
    create_stmt = "CREATE TABLE classification_totals (Classification VARCHAR(255), Totals VARCHAR(255))"
    DBUtil.create_table(create_stmt)
    # print(create_stmt)


# ------------- Main Program -------------#
def main():
    DBUtil.create_connection()
    run_pipeline()
    DBUtil.select_table("classification_totals")


if __name__ == "__main__":
    main()