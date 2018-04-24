"""
Run this script on coded data to train a model to identify the associated app from a text description.
This will save data models that can classify text to the trained categories. 
"""

import json

import numpy as np
import pandas as pd
import tables 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

input_file = "service_now_sample.csv"
# can do the yes to 1 in read_csv
df = pd.read_csv(input_file, header = 0)

# extract the needed categories
gear_df = df[['short_description', 'u_category_gear']]
# remove nulls
gear_df = gear_df.replace(np.nan, '', regex=True)

# The most frequently appearing apps in the data
# Column name and the app as it appears in the u_category_gear column
categories = {
    'eoffer_emod': 'eOffer/eMod - Electronic Offers/Electronic Modifications',
    'vcss': 'VCSS - Vendor Customer Self Service',
    'any_connect_windows': 'Cisco AnyConnect Windows Client 3.1',
    'easi': 'EASi - Electronic Acquisition System Integration',
    'google_email': 'Google Email',
    'pegasys_admin': 'Pegasys Admin Queries',
    'fss_online': 'FSS Online - Federal Supply Service Online',
    'etams': 'ETAMS - Electronic Time and Attendance Management System',
    'pegasys_data': 'PDE - Pegasys Data Entry',
    'aloha': 'Aloha - Authorized Leave and Overtime Help Application',
    'fmis': 'FMIS - Financial Management Information System',
    'apm': 'APM - Acquisition Planning Module',
    'google_docs': 'Google Docs',
    'google_chrome': 'Google Chrome',
    'ears': 'EARS - Enterprise Access Request System',
    'bookit': 'BookIt',
    'rocis': 'ROCIS - RISC/OIRA Consolidated Information System',
    'eviewer': 'eViewer',
    'google_calendar': 'Google Calendar',
    'geco': 'GECO - GSA Enhanced Checkout',
    'ors': 'ORS - Offer Registration System',
    'google_sites': 'Google Sites',
    'bi': 'BI - Business Intelligence Framework',
    'google_hangout': 'Google Hangout',
    'google_groups': 'Google Groups',
    'vitap': 'VITAP - Visual Invoice Tracking and Payment (FoxPro)',
    'ocms': 'OCMS - On-Line Contract Management System',
    'pegasys_vrm': 'Pegasys Vendor Request Management',
}

# add a column to the data frame for each category so we can evaluate them separately
for category_key in categories:
    gear_df[category_key] = np.where(gear_df['u_category_gear']==categories[category_key], 1, 0)

# vectorize description
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(gear_df['short_description'])
X_train_counts.shape

# shape data
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

def save_data_model(text_clf, app):
    file_name = "data_models/" + app + "_model.h5"
    store = pd.HDFStore(file_name)
    counter = 0
    for row in text_clf.coef_:
        store['row' + str(counter)] = pd.DataFrame(row)
        counter += 1
    store.close() 

# train and test for each category
for app in categories:
    formated_category = gear_df[[app]]
    text_clf = MultinomialNB().fit(X_train_counts,formated_category.values.ravel())
    save_data_model(text_clf, app)
    # test model
    predicted = text_clf.predict(X_train_counts)
    # print(app, np.mean(predicted == formated_category.values.ravel()))
    gear_df[app] = predicted

gear_df.to_csv('category_predictions_top_28.csv')
