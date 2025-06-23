import pandas as pd

# Load all tables from the "List of Family Guy episodes" Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_Family_Guy_episodes"
tables = pd.read_html(url)

# Filter only episode tables by checking for known column headers
episode_tables = [
    table for table in tables
    if 'No. overall' in table.columns
]

# Attach season numbers and combine all tables
all_episodes = []

for season_number, table in enumerate(episode_tables, start=1):
    table['Season'] = season_number  # Add season number column
    all_episodes.append(table)

# Concatenate into a single DataFrame
episodes_df = pd.concat(all_episodes, ignore_index=True)

# Preview the result
print(episodes_df[['Season', 'No. overall', 'Title']].head())

# Save to CSV
episodes_df.to_csv("family_guy_episodes_with_seasons.csv", index=False)
