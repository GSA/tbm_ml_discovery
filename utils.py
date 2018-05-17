
"""Exploratory functions used to clean and explore the data"""
import csv
import operator


def print_categories():
    """ Prints out categories and how many occurrences in the category """
    u_item_dict = {}
    with open('service_now_ticket_sample.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
            if row['u_category_gear'] not in u_item_dict:
                u_item_dict[row['u_category_gear']] = 1
            elif row["U_Category Match Found in GEAR?"] == "Yes":
                u_item_dict[row['u_category_gear']] = u_item_dict[row['u_category_gear']] + 1
    print(sorted(u_item_dict.items(), key=operator.itemgetter(1)))



def print_average_open():
    """Print average of how long tickets are open """
    days = 0
    incidents = 0

    with open('service_now_ticket_sample.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:             
            days = days + int(row['calendar_duration (days)'])
            incidents = 1 + incidents
            
            u_item_dict[row['u_category_gear']][0] = int(u_item_dict[row['calendar_duration (days)']])
            u_item_dict[row['u_category_gear']][0] += 1
            
    print(u_item_dict)
    for item in u_item_dict:
        print (item, item[0], item[1])


def load_category_mapping():
    category_map = {}
    subcategory_map = {}
    item_map = {}

    with open('Application_TableLookup.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            # gear_category then the matching terms
            category_map[line[0]] = line[1]
            subcategory_map[line[3]] = line[4]
            item_map[line[6]] = line[7]
    return(category_map, subcategory_map, item_map)
