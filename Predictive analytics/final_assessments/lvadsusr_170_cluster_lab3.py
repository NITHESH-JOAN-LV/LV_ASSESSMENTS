# -*- coding: utf-8 -*-
"""LVADSUSR_170_Cluster_LAB3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NkUFjV7gdEPTeqIAk0CPyK54FdLs-ams
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, explained_variance_score, r2_score

import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv('/content/customer_segmentation.csv')

df.head()

df.shape

df.columns

df.info()

df.duplicated().sum()

df.isnull().sum()

plt.hist(df['Income'])
plt.xlabel('Income')
plt.ylabel("Frequency")
plt.title("Histogram of Income")
plt.plot()

df['Income'].fillna(df['Income'].median(),inplace=True)

df.isnull().sum()

for col in df.select_dtypes([int,float]).columns:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

numerical=df.select_dtypes([int,float])
for i in range(len(numerical.columns)):
  for j in range(i+1,len(numerical.columns)):
    plt.scatter(df[numerical.columns[i]],df[numerical.columns[j]])
    plt.title(f'Scatter plot of {numerical.columns[i]} and {numerical.columns[j]}')
    plt.show()

from scipy import stats
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()
        z_scores = np.abs(stats.zscore(df[col]))
        threshold = 3
        outliers = np.where(z_scores > threshold)[0]
        print(f'Outliers in {col}: {outliers}')
        df[col].iloc[outliers] = df[col].mean()

df.head(3)

le = LabelEncoder()
df['Marital_Status']=le.fit_transform(df['Marital_Status'])

df.head(3)

corr_mat=df.drop(['ID','Year_Birth','Education','Dt_Customer','Recency','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','AcceptedCmp1'
,'AcceptedCmp2','Complain','Z_CostContact','Z_Revenue','Response'],axis=1).corr()

sns.heatmap(corr_mat,annot=True,fmt='.2f',cmap='viridis')
plt.show()

x=df.drop(['ID','Year_Birth','Education','Dt_Customer','Recency','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','AcceptedCmp1'
,'AcceptedCmp2','Complain','Z_CostContact','Z_Revenue','Response','MntMeatProducts','MntFishProducts',
          'MntSweetProducts','MntGoldProds','MntWines','MntFruits','Kidhome','Teenhome' ],axis=1)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(x)

df.columns

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(scaled_data)

  wcss.append(kmeans.inertia_)

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# from the elbow point the best number of cluster is 3
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=42)
Y=kmeans.fit_predict(scaled_data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=labels, s=50, cmap="viridis", alpha=0.8)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='o', s=110, label="Centroids")
plt.title("K-Means Clustering")
plt.legend()
plt.show()

from sklearn.metrics import silhouette_score
print('silhouette score')
print(silhouette_score(scaled_data,kmeans.fit_predict(scaled_data)))
print('kmean_inertia',kmeans.inertia_)

scaled_data[0]

plt.scatter(scaled_data[Y==0,0], scaled_data[Y==0,1], s=50, c='green', label='Cluster 1')
plt.scatter(scaled_data[Y==1,0], scaled_data[Y==1,1], s=50, c='red', label='Cluster 2')
plt.scatter(scaled_data[Y==2,0], scaled_data[Y==2,1], s=50, c='yellow', label='Cluster 3')


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')
plt.show()
