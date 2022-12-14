import pandas as pd
import seaborn as sns
sns.set(font_scale=1.3)
data = pd.read_csv('data.csv')
sns.scatterplot(x='Duration', y='Maxpulse', data=data)
