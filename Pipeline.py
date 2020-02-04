import re
import runner

""" data cleanup as per Problem 1 statement """
def data_cleanup(row):
    if re.match("([\d]+)[.]([\d]+)[.]([\d]+)$", row[0]):
        return row

""" data normalization as per problem 2 statement """
def normalize_row(cleaned_row):
    # print(cleaned_row[21].)
    if re.match(u'([\d]{4})$', cleaned_row[21]):
        print(cleaned_row[21], 'a')
    elif re.match(u'([\d]+)[-]([\d]+)$', cleaned_row[21]):
        print(cleaned_row[21], "b")
    elif re.match(u'^[0-9]+(-[0-9]+)+$', cleaned_row[21]):
        print(cleaned_row[21], "c")
    elif re.match("^[ca. ]([\d]+)", cleaned_row[21]):
        print(cleaned_row[21], "d")
    return cleaned_row

""" Calculate running totals as per problem 3 statement """
def running_total(normalized_row, running_total_dict):
    word = normalized_row[36]

    if word in running_total_dict:
        running_total_dict[word] += 1
    else:
        running_total_dict[word] = 1

