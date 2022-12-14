import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv('data.csv')
df['zscore'] = ( df.Calories - df.Calories.mean() ) / df.Calories.std()
df[df['zscore']>3]
