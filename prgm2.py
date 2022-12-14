import pandas as pd
df = pd.read_csv('data.csv')
df_new = df
print(df.isna().sum())
print(df.shape) 
df_new['Calories'] = df_new['Calories'].fillna((df_new['Calories'].mean()))
print(df_new.isna().sum())
print(df.shape)
