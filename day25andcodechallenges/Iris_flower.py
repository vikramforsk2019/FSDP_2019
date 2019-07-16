#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:37:46 2019

@author: vikram
"""


Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).

    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\
Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data




import numpy as np 
import pandas as pd 
import sklearn
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features_test)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = '1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = '2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = '3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of species')
plt.xlabel('pca 1')
plt.ylabel('pca 2')
plt.legend()
plt.show()


















