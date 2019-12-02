#%%
# read packages
import random
import numpy as np
import pandas as pd
import pandas_profiling

from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier


# set out seed 
np.random.seed(619)
#%%
# import OK cupid data
ok = pd.read_csv('https://www.dropbox.com/s/db8t2ywm4xmy4t6/okcupid.csv?dl=1')

#%%
# check the data format
# politics (target)
le_politics = preprocessing.LabelEncoder().fit(ok['q212813'].unique())
ok.loc[:,'politics'] = le_politics.transform(ok['q212813'])
# le_politics.inverse_transform([0,1,2])

# gender
le_gender = preprocessing.LabelEncoder().fit(ok['gender'].unique())
ok.loc[:,'gender'] = le_gender.transform(ok['gender'])

# income
le_income = preprocessing.LabelEncoder().fit(ok['d_income'].unique())
ok.loc[:,'income'] = le_income.transform(ok['d_income'])

# bodytype
le_bodytype = preprocessing.LabelEncoder().fit(ok['d_bodytype'].unique())
ok.loc[:,'bodytype'] = le_bodytype.transform(ok['d_bodytype'])

# race
le_race = preprocessing.LabelEncoder().fit(ok['race'].unique())
ok.loc[:,'race'] = le_race.transform(ok['race'])

# religion
le_religion = preprocessing.LabelEncoder().fit(ok['d_religion_type'].unique())
ok.loc[:,'religion'] = le_religion.transform(ok['d_religion_type'])

# hold out random portion for test
msk = np.random.rand(len(ok)) < 0.8
train = ok[msk]
test = ok[~msk]

#%%
# take a look at the data


#%%
# sample tree

# check out accuracy 



#%%
# bigger tree

# check out accuracy 
# in sample:

# out sample:


#%%
# Everything

# check out accuracy 
# in sample:

# out sample:


#%%
# Bagging

# check out accuracy 
# in sample:

# out sample:


#%%
# Random Forest

# check out accuracy 


#%%
# what features were important?


# Print the feature ranking

# graph it 


#%%
# Merging

# chop up the data first
# assign user ID
ok.loc[:, 'user_id'] = np.random.choice(range(1000, 10000), len(ok), replace=False)

# create copies with only certain columns
ok1 = ok.loc[:, ['user_id', 'age', 'religion', 'income']]
ok2 = ok.loc[:, ['user_id', 'race', 'politics', 'p_kinky']]

# delete randomly from each
n_remove = 200

drop_indices = np.random.choice(ok1.index, n_remove, replace=False)
ok1 = ok1.drop(drop_indices)

drop_indices = np.random.choice(ok2.index, n_remove, replace=False)
ok2 = ok2.drop(drop_indices)

# left merge 

# right merge 

# inner merge

# outer merge 


# Concatenate 
