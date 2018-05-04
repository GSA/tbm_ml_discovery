"""
Run this script on coded data to train a model to identify the associated app from a text description.
This will save data models that can classify text to the trained categories. 
"""
import json

import numpy as np
import pandas as pd
import tables 

from apps import categories

# would like to load from data in next iteration
from sklearn.externals import joblib
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

# add a column to the data frame for each category so we can evaluate them separately
for category_key in categories:
    gear_df[category_key] = np.where(gear_df['u_category_gear']==categories[category_key], 1, 0)

# vectorize description
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(gear_df['short_description'])
X_train_counts.shape

# shape data
tfidf_transformer = TfidfTransformer()
X_train_counts = count_vect.fit_transform(gear_df['short_description'])
# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


# X_train_tfidf.shape


def save_data_model(text_clf, app):
    # want to save as data in the future
    file_name = "data_models/" + app + "_model.pkl"
    joblib.dump((text_clf), file_name) 


# train and test for each category
for app in categories:
    formated_category = gear_df[[app]]
    text_clf = MultinomialNB().fit(X_train_counts,formated_category.values.ravel())

    save_data_model(text_clf, app)
    predicted = text_clf.predict(X_train_counts)
    # nice output on the effectiveness of the models
    print(app, np.mean(predicted == formated_category.values.ravel()))
    gear_df[app] = predicted


gear_df.to_csv('category_predictions_top_28.csv')


# # I might want to take care of this earlier, but will write it out here
# def decode_app(row):
#     for app in categories:
#         if row[app] == 1:
#             row[app] = categories[app]
#     else:
#         row['category_label'] = 'undefined'

# gear_df['prediction_of_category'] = gear_df.apply(lambda row: decode_app(row), axis=1)


# gear_df.to_csv('category_predictions_with_label.csv')


""" seperate inot another file """


input_file = "20180501_ServiceNow_INC_Tickets.csv"
# can do the yes to 1 in read_csv
df = pd.read_csv(input_file, header = 0)

# remove nulls
new_df = df.replace(np.nan, '', regex=True)


# add a column to the data frame for each category so we can evaluate them separately
for category_key in categories:
    new_df[category_key] = ''


X_train_counts = count_vect.transform(new_df['short_description'])

for app in categories:
    file_name = 'data_models/{}_model.pkl'.format(app)
    text_clf = joblib.load(file_name) 
    predicted = text_clf.predict(X_train_counts)
    new_df[app] = predicted

def decode_app(row):
    field = ''
    for app in categories:
        if row[app] == 1:
            field = categories[app]
    if field == '':
        field = 'undefined'
    return field

new_df['prediction_of_category'] = new_df.apply(lambda row: decode_app(row), axis=1)

# remove temporary rows
new_df = new_df.drop(columns=[app for app in categories])

new_df.to_csv('categorized_output_1.csv')

