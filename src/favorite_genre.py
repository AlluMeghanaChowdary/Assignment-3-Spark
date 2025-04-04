import pandas as pd
import os

os.makedirs("output", exist_ok=True)

logs = pd.read_csv("input/listening_logs.csv")
songs = pd.read_csv("input/songs_metadata.csv")
data = logs.merge(songs, on="song_id")

favorite_genres = (
    data.groupby(['user_id', 'genre'])
    .size()
    .reset_index(name='play_count')
    .sort_values(['user_id', 'play_count'], ascending=[True, False])
)

favorite_per_user = favorite_genres.groupby('user_id').first().reset_index()
favorite_per_user.to_csv("output/favorite_genre.csv", index=False)