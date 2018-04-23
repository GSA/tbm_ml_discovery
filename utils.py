
"""Exploratory functions used to explore the data"""
import csv

""" Prints out categories and how many you see """
def print_categories():
    u_item_dict = {}

    with open('service_now_ticket_sample.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:             
            if row['u_category_gear'] not in u_item_dict and row["U_Category Match Found in GEAR?"] == "Yes":
                u_item_dict[row['u_category_gear']] = 1
            elif row["U_Category Match Found in GEAR?"] == "Yes":
                u_item_dict[row['u_category_gear']] = u_item_dict[row['u_category_gear']] + 1

    print(u_item_dict)


"""print average of how long tickets are open """
def print_average_open():
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
        