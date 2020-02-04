import csv,re
import sys,os

sys.path.append(os.getcwd())

import DBUtil, Pipeline

class Runner:

    global insert_columns
    insert_columns = None

    def __init__(self, data_file):
        self.data_file = data_file
        self.running_total_dict = {}
        self.dbobj = DBUtil.DBUtil(r"pythonsqlite.db", None)


    def run_pipeline(self):
        with open(self.data_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_num = 0


            for row in csv_reader:

                if line_num == 0:

                    self.setup_tables(row, insert_columns) # Create both table here with column names with headers available in 0th row
                    line_num += 1
                else:
                    cleaned_row = Pipeline.data_cleanup(row) # Step 1: data cleanup for first column

                    if cleaned_row is not None:  # Step 2: Normalize the date column

                        date_range = Pipeline.normalize_row(cleaned_row[21])

                        insert_stmt = "INSERT INTO data_normalized(" + insert_columns_a + ") VALUES(" \
                                      + '"{0}"'.format('", "'.join(cleaned_row)) + ",\"" \
                                      + date_range[0]+ "\", \"" + date_range[1] +"\")"

                        self.dbobj.insert_table(insert_stmt)

                        Pipeline.running_total(cleaned_row, self.running_total_dict) # Step 3: Calculate running_total

                    line_num += 1
                    #if line_num == 2000:
                        #break;

            # Populate classification_totals table with calculated running totals
            for classification, totals in self.running_total_dict.items():
                insert_stmt = "INSERT INTO classification_totals(Classification, Totals) VALUES (\"" \
                              + classification +"\",\""+ str(totals) +"\")"

                self.dbobj.insert_table(insert_stmt)

            self.dbobj.commit()
            #self.dbobj.select_table("data_normalized")
            #self.dbobj.select_table("classification_totals")


    def setup_tables(self, row, insert_columns):

        self.dbobj.create_connection()
        # Create query statement for data_normalized table with two additional columns
        tup = tuple(word.replace(" ", "_") for word in row)
        global insert_columns_a
        insert_columns_a = f'{", ".join(tup)}' + ', Object_Start_date' + ', Object_End_date'
        create_columns = f'{" VARCHAR(255), ".join(tup)}'
        create_stmt = "CREATE TABLE data_normalized (" + create_columns + \
                      " VARCHAR(255), Object_Start_date VARCHAR(255), Object_End_date VARCHAR(255))"

        # Create data_normalized table
        self.dbobj.drop_table('data_normalized')
        self.dbobj.create_table(create_stmt)

        # Create classification_totals table
        self.dbobj.drop_table('classification_totals')
        create_stmt = "CREATE TABLE classification_totals (Classification VARCHAR(255), Totals VARCHAR(255))"
        self.dbobj.create_table(create_stmt)


# ------------- Main Program -------------#
def main():
    runobj = Runner(r"DataEngineerDataSet.csv")
    runobj.run_pipeline()


if __name__ == "__main__":
    main()

