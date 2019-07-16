#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:24:49 2019

@author: vikram
"""

Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

                    Impute the missing values with the most frequent values.
                    Perform Classification on the given data-set to predict if the tumor is cancerous or not.
                    Check the accuracy of the model.
                    Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("breast_cancer.csv")



most_freq=dataset['G'].mode()

dataset['G'].value_counts()
   
dataset['G'] = dataset['G'].replace(np.nan,most_freq[0])

features = dataset.iloc[:, 1:-1].values
labels = dataset.iloc[:, -1].values


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

x=np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1);

labels_pred2=classifier.predict(x)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)


"""
Predict whether a women has Benign tumor or Malignant tumor, 
if her Clump thickness is around 6, 
uniformity of cell size is 2, 
Uniformity of Cell Shape is 5, Marginal Adhesion is 3, 
Bland Chromatin is 9,
 Mitoses is 4, Bare Nuclei is 7, 
 Normal Nuclei is 2 and Single Epithelial Cell Size is 2

"""










