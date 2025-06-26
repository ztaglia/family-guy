import pandas as pd

df = pd.read_csv('family_guy_dialogue_sentiment.csv')

print(df.head())

# 155242 rows
print(df.shape[0])

# checking number of episodes per season
print(df.groupby('Season')['Episode'].nunique())
