import pandas as pd

df = pd.DataFrame(data)
df.index
df.columns
df.values
df.T

# Selection
df['columnID']
df[['columnID1','columnID2']]	
df.columnID	
df[0:3]	
df['columnID'][:5]	
df.loc[] ==> by label	
	df.loc[dates[0]]
	df.loc[:,['A','B']]
	df.loc['20130102':'20130104',['A','B']]
df.iloc[] ==> by position	
	df.iloc[3]
	df.iloc[3:5,0:2]
	df.iloc[[1,2,4],[0,2]]

# Functions
df.head()	
df.tail()	
df.describe()	
df.mean()	
df['columnID'].value_counts()	
df.sort_values()	
	df.sort_values(by='columnID')
df.apply()	
	df.apply(np.cumsum)
	df.apply(lambda x: x.max() - x.min())
df.set_index('columnID')

# Filtering
df[df.A > 0]	
df[df > 0]	
	df[df > 0 & df < 10]
df[df['columnID'].isin(list)]	
	df[df['A'].isin(['apple','orange'])]
