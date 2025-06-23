import pandas as pd
import os
import chardet
from imdb import Cinemagoer

ia = Cinemagoer()

def get_document_path(doc_name):
    current_directory = os.path.dirname(__file__)
    document_name = doc_name
    document_path = os.path.join(current_directory, document_name)
    return document_path

# Family Guy's movie id is 0182576
movie_id = '0182576'

# input movie id from url (Family Guy)
movie = ia.get_movie('0182576')

df = pd.read_csv(get_document_path('episode-basics.tsv'), sep='\t', header=1, on_bad_lines='skip')
df.drop(0, inplace=True)

fg_df = df.loc[df['parentTconst'] == 'tt' + movie_id]
print(fg_df.head(10))

# numbers are string formatted, we need to change this 
fg_df = fg_df.sort_values('seasonNumber', ascending=True)
print(fg_df.head(10))

# changed to int 
fg_df[['seasonNumber', 'episodeNumber']] = fg_df[['seasonNumber', 'episodeNumber']].astype(int)
fg_df = fg_df.sort_values(by=['seasonNumber', 'episodeNumber'], ascending=[True, True])
print(fg_df.head(10))

def extract_episode_info(row):
    movie = ia.get_movie(row['tconst'])
    title = movie['title']
    year = movie['year']
    plot = movie['plot']
    print(pd.Series({'Episode Title': title, 'Release Year': year, 'Episode Summary': plot}))
    return pd.Series({'Episode Title': title, 'Release Year': year, 'Episode Summary': plot})

# use Cinemagoer API
fg_df['tconst'] = fg_df['tconst'].str.replace(r'^tt', '', regex=True)
fg_df['parentTconst'] = fg_df['parentTconst'].str.replace(r'^tt', '', regex=True)
print(fg_df.head(10))
new_cols = fg_df.apply(extract_episode_info, axis=1)
fg_df = pd.concat([fg_df, new_cols], axis=1)
print(fg_df.head(10))

fg_df.to_csv('fg_df_unfinished.csv', index=False)
