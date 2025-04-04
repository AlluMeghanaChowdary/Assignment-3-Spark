import pandas as pd
import os

os.makedirs("output", exist_ok=True)

logs = pd.read_csv("input/listening_logs.csv")
songs = pd.read_csv("input/songs_metadata.csv")
logs['timestamp'] = pd.to_datetime(logs['timestamp'])
data = logs.merge(songs, on="song_id")

week_data = data[(data['timestamp'] >= '2025-03-23') & (data['timestamp'] <= '2025-03-30')]

top_songs = (
    week_data.groupby(['song_id', 'title'])
    .size()
    .reset_index(name='play_count')
    .sort_values(by='play_count', ascending=False)
    .head(10)
)

top_songs.to_csv("output/top_10_this_week.csv", index=False)