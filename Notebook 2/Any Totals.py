with open("US_births_1994-2003_CDC_NCHS.csv") as f:
    data = f.read().split("\r")

# This takes a clean file and splits into a list of lists.
def read_csv(filename):
    string_list = open(filename).read().split("\r")[1:]
    final_list = []
    for i in string_list:
        string_fields = i.split(",")
        int_fields = []
        for x in string_fields:
            int_fields.append(int(x))
        final_list.append(int_fields)
    return final_list

'''
# This takes a list of lists, and returns a dictionary
def month_births(list_of_lists):
    births_per_month = {}
    for i in list_of_lists:
        if i[1] in births_per_month:
            births_per_month[i[1]] += i[4]
        else:
            births_per_month[i[1]] = i[4]
    return births_per_month
# This takes a list of lists, and returns a dictionary
def dow_births(list_of_lists):
    day_of_week = {}
    for i in list_of_lists:
        if i[3] in day_of_week:
            day_of_week[i[3]] += i[4]
        else:
            day_of_week[i[3]] = i[4]
    return day_of_week
'''

# The last two functions are so similar..This is a more general function that does both.
def calc_counts(data, column):
    td = {}
    for i in data:
        if i[column] in data:
            td[i[column]] += i[4]
        else:
            td[i[column]] = i[4]
    return td

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)