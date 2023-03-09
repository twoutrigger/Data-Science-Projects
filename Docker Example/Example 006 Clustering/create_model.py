import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import joblib
import pickle

df = pd.read_csv('../../Datasets/glass.data', header=None, index_col=0)

int_to_str = {1: 'building window 1', 2: 'building window 2',
              3: 'car window 1', 4: 'car window 2',
              5: 'glass containers', 6: 'tableware', 7: 'headlamps'}

df.iloc[:, -1] = df.iloc[:, -1].map(int_to_str)

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

scaler = MinMaxScaler()
x = scaler.fit_transform(x)

# print(type(x))
# print(x[0])

# save minmax scaler for transforming test data
scaler_filename = "minmaxscaler.save"
joblib.dump(scaler, scaler_filename)

km = KMeans(n_clusters=3, max_iter=2000, algorithm = 'auto')
km.fit(x)

test = km.predict(x)
print(test)

# print(x[0])
# print(df.head(5))

# print(km.labels_)
# print(len(km.labels_))

df['label'] = km.labels_

## could try silhouette_method to improve grouping
## research pickling of data normalization
print(df.groupby(['label', 10]).size())

## pickle k-means model
pickle_save = 'kmeans.pkl'
with open(pickle_save, 'wb') as file:
    pickle.dump(km, file)

## test out prediction
# pred = km.predict(x)
# print(pred)