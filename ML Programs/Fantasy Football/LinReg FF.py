#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import linear_model
from statsmodels.api import OLS
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso


dataset = pd.read_csv('train75.csv')
print(dataset.shape)
print(dataset.describe())

#dataset.isnull().any()
#dataset = dataset.fillna(method='ffill')
#l_owners_17

vals = ['l_owners17', 'l_recepts17','off_passydsg17', 'off_runydsg17', 'off_linepff18', 'l_recydgm17', 'l_passydgm17', 'l_rushydgm17', 'l_td_square', 'ppg_17']

null_set = []
for i in range(len(vals)):
    null_vals = dataset[vals[i]].isna()
    for j in range(len(null_vals)):
        if(null_vals[j] and (j not in null_set)):
            null_set.append(j)

dataset = dataset.drop(null_set)

X = dataset[vals].values
y = dataset['l_points18'].values
plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['l_points18'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)



#Summary Stats
print(OLS(y_train,X_train).fit().summary())



print("Lasso Predict with transformations")
clf = linear_model.Lasso(alpha=1)


clf.fit(X_train, y_train)
coeff_df1=pd.DataFrame(clf.coef_)
print(coeff_df1)
print(clf.intercept_)
y_pred = clf.predict(X_test)

dfLasso = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
#print(dfLasso)
 
dfLasso.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[58]:


coeff_df1


# In[59]:


print(OLS(y_train,X_train).fit().summary())


# In[ ]:




