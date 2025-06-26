import pandas as pd

df = pd.read_csv('family_guy.csv')

# Split & explode Directed By
df['Directed by'] = df['Directed by'].str.split('&')
df = df.explode('Directed by')
df['Directed by'] = df['Directed by'].str.strip()

# Split & explode Written By
df['Written by'] = df['Written by'].str.split('&')
df = df.explode('Written by')
df['Written by'] = df['Written by'].str.strip()

df[['No. in season', 'No. overall', 'Season']] = df[['No. in season', 'No. overall', 'Season']].fillna(-1).astype(int)



df.to_csv('family_guy_cleaned.csv', index=False)