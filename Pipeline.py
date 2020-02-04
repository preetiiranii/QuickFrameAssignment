import re
import runner

""" data cleanup as per Problem 1 statement """
def data_cleanup(row):
    if re.match("([\d]+)[.]([\d]+)[.]([\d]+)$", row[0]):
        return row
    

""" data normalization as per problem 2 statement """
def normalize_row(date):
    if re.match(u'()([\d]{4})$', date):
          return(date, date)

    elif re.match(u'([\d]{4})[–]([\d]{2})$', date):
          return(normalize_dates(date, '–'))

    elif re.match(u'([\d]{4})[–]([\d]{4})$', date):
          return(normalize_dates(date, '–'))

    elif re.match(u'(^ca.)([\d]{4})$', date):
          return(normalize_dates(date, 'ca.'))

    else:
          return (date, date)

""" Calculate running totals as per problem 3 statement """
def running_total(normalized_row, running_total_dict):
    word = normalized_row[36]

    if word in running_total_dict:
        running_total_dict[word] += 1
    else:
        running_total_dict[word] = 1

""" Split the date range """
def normalize_dates(data, separator):
    year = data.split(separator)

    if separator == '–':
        year1 = year[1]
        if len(year[1]) == 2:
            year[1] = year[0][0:2] + year1

    elif separator == 'ca.':
        year[0] = str(int(year[1]) - 3)

    return(year)