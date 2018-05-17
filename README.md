This project aims to use machine learning to reduce processing times for TBM data. 

## Set up

Make sure you have python and dependencies installed. This project uses [pipenv](https://docs.pipenv.org/)

To start, you can look at the notebook where I hammered out the basics, run:

```
jupyter notebook
```

To train the data model, get the training sample data as a csv and name that file `service_now_sample.csv`. There is a simple excel to csv converter in utils.py if you need it.

To train and test the data models run:

```
python tbm_calssifier.py
```

That will train models to recognize the app associated with the record based on the short description. It stores each model in `/data_models` as a HDF5 file. It will then take an new file and make the classifications. 





## Background

This is inspired by Atul Varma's work on OMB
https://github.com/toolness/omb-policy-ml-fun/blob/master/omb-policy-fun.ipynb


Other helpful resources

https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a

http://thiagomarzagao.com/2015/12/07/model-persistence-without-pickles/

http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py

https://pypi.org/project/joblib/