import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'twitter_dataset.csv'

df = pd.read_csv(file_path)

df = df[(df['retweets'] > 20000) & (df['lang'] == 'en')]

sns.pairplot(df, hue="case")
plt.show()