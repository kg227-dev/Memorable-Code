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
ok = pd.read_csv('okcupid.csv')

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
profile = train.profile_report()
profile.to_file(output_file='report.html')

#%%
# sample tree
X = train.loc[:, ['income']]
X = X.to_numpy().reshape(-1,1) # if only 1
Y = train['politics']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
# check out accuracy 
test_X = test.loc[:, ['income']]
test_X = test_X.to_numpy().reshape(-1,1)

pred = clf.predict(test_X)
accuracy_score(test['politics'], pred)


#%%
# bigger tree
feats = ['race', 'religion', 'income'] 
X = train.loc[:, feats]
Y = train['politics']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
# check out accuracy 
# in sample:
pred = clf.predict(train.loc[:, feats])
accuracy_score(train['politics'], pred)
# out sample:
pred = clf.predict(test.loc[:, feats])
accuracy_score(test['politics'], pred)

#%%
# Everything
all_feat = ['race'
            , 'gender'
            , 'religion'
            , 'income'
            , 'bodytype'
            , 'p_kinky'
            , 'p_artsy'
            , 'p_scien']

X = train.loc[:, all_feat]
Y = train['politics']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
# check out accuracy 
# in sample:
pred = clf.predict(train.loc[:, all_feat])
accuracy_score(train['politics'], pred)
# out sample:
pred = clf.predict(test.loc[:, all_feat])
accuracy_score(test['politics'], pred)


#%%
# Bagging
X = ok.loc[:, all_feat]
Y = ok['politics']
bag = BaggingClassifier(n_estimators=1000, oob_score=True)
bag = bag.fit(X, Y)
# check out accuracy 
# in sample:
pred = bag.predict(ok.loc[:, all_feat])
accuracy_score(ok['politics'], pred)
# out sample:
bag.oob_score_

#%%
# Random Forest
X = ok.loc[:, all_feat]
Y = ok['politics']
rf = RandomForestClassifier(n_estimators=10000, oob_score=True)
rf = rf.fit(X, Y)
# check out accuracy 
rf.oob_score_

#%%
# what features were important?
importances = rf.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# graph it 
import matplotlib.pyplot as plt
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()

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
