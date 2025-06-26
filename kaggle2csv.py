import pandas as pd

df = pd.read_csv('family_guy_dialogue_sentiment.csv')

print(df.head())

# 155242 rows
print(df.shape[0])

# checking number of episodes per season
print(df.groupby('Season')['Episode'].nunique())

# checking number of Dialogue datapoints per episode
print(df.groupby(['Season', 'Episode'])['Dialogue'].count())

dialogue_per_episode = df.groupby(['Season', 'Episode'])['Dialogue'].count().reset_index()
dialogue_per_episode.to_csv('episode_dialogue_counts.csv', index=False)
