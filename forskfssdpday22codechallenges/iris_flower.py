#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:57:55 2019

@author: vikram
"""

"""
Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper,
 The Use of Multiple Measurements in Taxonomic Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm classifier 
and use the trained svm model to predict the Iris species type.
 To begin with let’s try to load the Iris dataset.
 """
 
 
import numpy as np 
import pandas as pd 
import sklearn
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


#Import dataset and create a dataframe

from sklearn import datasets
iris= datasets.load_iris()

print(iris.DESCR)

iris_df	= pd.DataFrame (iris.data, columns= iris.feature_names )
iris_df.head()
iris_df['species type']= iris.target
features = iris_df.iloc[:, :-1].values
labels = iris_df.iloc[:, -1].values
 

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)



from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)
 
 
 
 
#Visualization

x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))
# Obtain labels for each point in mesh using the model.
# ravel() is equivalent to flatten method.
# data dimension must match training data dimension, hence using ravel
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
#do not print bcoz 4-d data set 
# Plot the points
plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')
#plot the decision boundary
plt.contourf(xx, yy, Z, alpha=1.0)

plt.show()


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

 
gnb = GaussianNB()

gnb.fit(features_train,labels_train)
 
labels_pred = gnb.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(labels_test, labels_pred)

from sklearn import metrics

print("Accuracy:",metrics.accuracy_score(labels_test, labels_pred))
 
 
 