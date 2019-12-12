import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# grab football data -- change path for your own file
df1 = pd.read_csv("/Users/kushgulati/Desktop/Memorable-Code/Miscellaneous Programs/train75.csv")

# print first few rows -- could also use df.head()
print (df1.iloc[:3])
# and get summary stats on variables
print (df1.describe())

# create set of variables to pass to PCA
vars = ['l_passyds17', 'l_passtd17', 'l_passint17', 'l_rushyds17', 'l_rushtd17']
x = df1.loc[:, vars].values

df2 = df1.dropna()
x2 = df2.loc[:, vars].values

# check to look for mistakes -- note the missingness
print ("X with na's")
print (x[:10])
print()
print ("X2 without na's")
print (x2[:10])
# note the drop in N
print (df2.describe())
# print (df1['l_passyds17'])

# standardize x2
x2 = StandardScaler().fit_transform(x2)


pca1 = PCA(n_components=2)

# create 2 dimensional representation
latent_vars = pca1.fit_transform(x2)
print ("Variance explained by each latent variable in PCA: ", pca1.explained_variance_ratio_)

#print latent variables, which can be used downstream in models instead of x
print(latent_vars)

# check components to see if they make sense
print (vars)
print (pca1.components_)

# create new dataframe with the latent variables from pca1
df2['pca1'] = latent_vars[:,0]
df2['pca2'] = latent_vars[:,1]

print ()
print (df2.iloc[:10])

