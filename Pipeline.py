import re
import runner

""" data cleanup as per Problem 1 statement """
def data_cleanup(row):
    if re.match("([\d]+)[.]([\d]+)[.]([\d]+)$", row[0]):
        return row
    #else:
        #print(row)

""" data normalization as per problem 2 statement """
def normalize_row(date):
    #print(cleaned_row[21])
    if re.match(u'()([\d]{4})$', date):
          #match=re.match(u'()([\d]{4})$', cleaned_row[21])
          #print(match.group(2))
          return(date, date)

    elif re.match(u'([\d]{4})[–]([\d]{2})$', date):
          #match=re.match(u'([\d]{4})[–]([\d]{2})$', cleaned_row[21])
          #print(match.group())
          #print(cleaned_row[21], 'b')
          return(normalize_dates(date, '–'))

    elif re.match(u'([\d]{4})[–]([\d]{4})$', date):
          #match = re.match(u'([\d]{4})[–]([\d]{4})$', cleaned_row[21])
          #print(match.group())
          #print(cleaned_row[21], 'c')
          return(normalize_dates(date, '–'))

    elif re.match(u'(^ca.)([\d]{4})$', date):
          #match=re.match(u'(^ca)\w+([\d]{4})', cleaned_row[21])
          #print(match.group())
          #print(cleaned_row[21], 'd')
          return(normalize_dates(date, 'ca.'))

    else:
          print(date)
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