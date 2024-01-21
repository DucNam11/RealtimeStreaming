import json
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer



#Loading and preprocess
train = pd.read_csv('datasets/train.csv', names= ('class','text'))
test = pd.read_csv('datasets/test.csv', names= ('class','text'))
train.loc[train["class"] == 1, "class"] = 0
train.loc[train["class"] == 2, "class"] = 1
test.loc[test["class"] == 1, "class"] = 0
test.loc[test["class"] == 2, "class"] = 1

svc_texts = list(train['text'])
svc_labels = list(train['class'])

#Feature extraction
vectorizer = TfidfVectorizer(ngram_range=(1,2), min_df=3)
Xs = vectorizer.fit_transform(svc_texts)

#Spliting data
Xs_train, Xs_test, ys_train, ys_test = train_test_split(Xs, np.array(svc_labels), test_size=0.4)

#Model initialization and trainng
svc_classifier = LinearSVC(max_iter=5000)
svc_classifier.fit(Xs_train, ys_train)