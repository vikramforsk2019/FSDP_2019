#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:01:27 2019

@author: vikram
"""


In an experiment with a group of 30 volunteers within an age bracket of 19 to 48 years, each person performed six activities (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. The experiments have been video-recorded to label the data manually.

The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data.

 

Attribute information

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration.
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:

  (a) a decision tree approach,

  (b) a random forest approach and

  (c) a logistic regression.

  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach on both the testing and training data set. Compare the results. Which approach would you recommend and why?

        Perform feature selection and repeat the previous step. Does your accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches taken with and without feature selection.

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


dataset = pd.read_csv('train.csv', delimiter = ',')
dataset2 = pd.read_csv('test.csv', delimiter = ',')





features_train = dataset.values[:,0:-1] 
labels_train = dataset.values[:,-1]  

features_test = dataset2.values[:,0:-1] 
labels_test = dataset2.values[:,-1]  

acc_score=[]
#first-DT  by default use gini index
# clf_gini = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=3, min_samples_leaf=5) 

#Decision tree with entropy 
# clf_entropy = DecisionTreeClassifier( criterion = "entropy", random_state = 100, max_depth = 3, min_samples_leaf = 5) 
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier(criterion = "gini")  
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test) 
acc_score.append(accuracy_score(labels_test, labels_pred))

#gini
classifier2 = DecisionTreeClassifier(criterion = "entropy")  
classifier2.fit(features_train, labels_train)
labels_pred = classifier2.predict(features_test) 
print(accuracy_score(labels_test, labels_pred))


#train the model _Random Forest

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0,criterion = "gini")  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)
acc_score.append(accuracy_score(labels_test, labels_pred))

classifier2 = DecisionTreeClassifier(n_estimators=10, random_state=0,criterion = "entropy")  
classifier2.fit(features_train, labels_train)
labels_pred = classifier2.predict(features_test) 
print(accuracy_score(labels_test, labels_pred))




# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
acc_score.append(accuracy_score(labels_test, labels_pred))


# Fitting KNN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 10, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
acc_score.append(accuracy_score(labels_test, labels_pred))


#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.


print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  




	

 
# 14 categories of movies
index = ['DT', 'RF', 'LR','KNN']


plt.bar(index, acc_score)
plt.xlabel('activity type', fontsize=15)
plt.ylabel('Activity Accuracy', fontsize=15)
#plt.xticks(acc_score, index, fontsize=10, rotation=45)
plt.title('Humanc Activity')
plt.show()


#by using features selection - backword elimination 
#label encode
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)

       
import statsmodels.api as sm

labels= dataset.values[:,-1]  
features_obj =dataset.values[:,0:-1] 
features_obj = sm.add_constant(features_obj)
while (True):
    regressor_OLS = sm.OLS(endog = labels_train,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break
    
regressor_OLS.summary()



#by using features selection  by using pca
# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

#give very poor result

print(accuracy_score(labels_test, labels_pred))


















































