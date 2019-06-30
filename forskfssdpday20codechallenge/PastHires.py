#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:27:25 2019

@author: vikram
"""
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""
import pandas as pd  
import numpy as np  

dataset = pd.read_csv("PastHires.csv")  


dataset.head()

#Preparing the dataset

#dataset["Employed?"] = dataset["Employed?"].map(lambda x: 1 if x =='Y' else 0 )

features = dataset.drop('Hired', axis=1).values 
labels = dataset['Hired'].values  


from sklearn.preprocessing import LabelEncoder
labelencoder1 = LabelEncoder()
features[:, 1] = labelencoder1.fit_transform(features[:, 1])

labelencoder2 = LabelEncoder()
features[:, 3] = labelencoder2.fit_transform(features[:, 3])


labelencoder3 = LabelEncoder()
features[:, 4] = labelencoder2.fit_transform(features[:, 4])


labelencoder4 = LabelEncoder()
features[:, 5] = labelencoder2.fit_transform(features[:, 5])

labelencoder5=LabelEncoder()
labels=labelencoder5.fit_transform(labels)



from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#using random forest
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 
#Q.1
x=np.array([10,1,4,0,1,0]).reshape(1,-1)
labels_pred = classifier.predict(x) 
# Q.2

x1=np.array([10,0,4,1,1,0]).reshape(1,-1)
labels_pred = classifier.predict(x1) 
print(labels_pred[0])
#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
cm=confusion_matrix(labels_test, labels_pred)

print('Accuracy of DT model::',(cm[1][1]/len(features_test))*100)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(accuracy_score(labels_test, labels_pred)*100)

"""
Q.1
y-1
n-0
bs-0,ms-1,phd-2
Predict employment of a currently employed 10-year veteran, 
previous employers 4, 
went to top-tire school, 
having Bachelor's Degree without Internship.

Q.2
    Predict employment of an unemployed 10-year veteran,
    ,previous employers 4, 
    didn't went to any top-tire school, 
    having Master's Degree with Internship.

"""
#using random forest
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 

#train the model

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred)*100)
  
#Q.1
x=np.array([10,1,4,0,1,0]).reshape(1,-1)
labels_pred = classifier.predict(x) 

# Q.2

x1=np.array([10,0,4,1,1,0]).reshape(1,-1)
labels_pred = classifier.predict(x1) 
print(labels_pred[0])
