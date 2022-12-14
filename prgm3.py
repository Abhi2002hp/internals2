import pandas as pd
df = pd.read_csv('data.csv')
dup=df.duplicated().sum()
print('No of duplicated rows:',dup)
print('No of rows in dataframe:',df.shape[0])
df_new = df
df_new=df_new.drop_duplicates()
dup1=df_new.duplicated().sum()
print('No of rows after deletion',dup1)
print('No of rows in dataframe:',df_new.shape[0])
