import pandas as pd

df = pd.read_csv('family_guy_dialogue_sentiment.csv')

print(df.head())

afinn_per_episode = df.groupby(['Season', 'Episode'])['AFINN_Sentiment_Score'].sum()

print(afinn_per_episode.head())

bing_word_counts = df.groupby(['Season', 'Episode'])['BING_Sentiment'].value_counts()

print(bing_word_counts.head())

# split nrc sentiments
df['NRC_Sentiment_List'] = df['NRC_Sentiment'].fillna('').apply(lambda x: [i.strip() for i in x.split(',') if i.strip()])

# explode the list into separate rows
df_exploded = df.explode('NRC_Sentiment_List')

# Group by Season, Episode, and NRC word → count frequency
nrc_word_counts = df_exploded.groupby(['Season', 'Episode', 'NRC_Sentiment_List']).size().reset_index(name='Frequency').reset_index()

print(nrc_word_counts.head())

nrc_word_counts.to_csv('nrc_sentiment_word_counts.csv', index=False)
bing_word_counts.to_csv('bing_sentiment_word_counts.csv', index=False)
afinn_per_episode.to_csv('afinn_sentiment_sums.csv', index=False)
