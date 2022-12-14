import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
plt.figure(figsize = (8,6))
sb.heatmap(df.isnull(), cbar=False , cmap = 'magma')
 
