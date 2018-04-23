"""
Simple helper script to format these to csv 

$ python convert_xls_to_csv name_of_file_without_extension
"""
import sys

import pandas as pd

file_name_no_extension=sys.argv[1]
excel_file = file_name_no_extension + '.xlsx'
csv_file = file_name_no_extension + '.csv'

data_xls = pd.read_excel(excel_file, '20180301_ServiceNow_INC_Tickets', index_col=None)
data_xls.to_csv(csv_file, encoding='utf-8')
