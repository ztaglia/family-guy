import pandas as pd
import requests

API_KEY = 'f68fb7e2ce6442b1ec291cbc18070a96'
TV_ID = 1434  # Family Guy TMDb ID

def get_tmdb_ratings(season):
    url = f"https://api.themoviedb.org/3/tv/{TV_ID}/season/{season}?api_key={API_KEY}"
    response = requests.get(url).json()
    print(response)

    episode_list = []

    for ep in response.get("episodes", []):
        print(f"{ep['episode_number']}. {ep['name']} | Air date: {ep['air_date']} | Rating: {ep['vote_average']}")
        ep_details = {
            'Season Number': season,
            'Episode Number': ep['episode_number'],
            'Episode Name': ep['name'],
            'Air Date': ep['air_date'],
            'Rating': ep['Rating'],
            'Epidsode Overview': ep['overview']
        }
        
    



df = get_tmdb_ratings(1)

