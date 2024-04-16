import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import  RandomForestClassifier

import numpy as np

# iris_df = pd.read_csv('iris.csv')
#
# y = iris_df['species']
# X = iris_df.drop('species', axis=1)
#
# kn = KNeighborsClassifier()
# model_kn = kn.fit(X, y)
#
# joblib.dump(model_kn, 'model_kn.pkl')

model_kn = joblib.load('model_kn.pkl')

# 예측
X_new = np.array([[2, 1, 2, 1]])
prediction = model_kn.predict(X_new)
print(f'KN prediction={prediction}')
probability = model_kn.predict_proba(X_new)
print(f'KN prob={probability}')

#새로운 모델
# rfc = RandomForestClassifier()
# model_rfc = rfc.fit(X, y)
#
# prediction = model_rfc.predict(X_new)
# print(f'RFC prediction={prediction}')
# probability = model_rfc.predict_proba(X_new)
# print(f'RFC prob={probability}')