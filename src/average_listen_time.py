import pandas as pd
import os

os.makedirs("output", exist_ok=True)

logs = pd.read_csv("input/listening_logs.csv")
songs = pd.read_csv("input/songs_metadata.csv")
data = logs.merge(songs, on="song_id")

avg_duration = (
    data.groupby(['song_id', 'title'])['duration_sec']
    .mean()
    .reset_index(name='average_duration_sec')
    .sort_values(by='average_duration_sec', ascending=False)
)

avg_duration.to_csv("output/average_listen_time.csv", index=False)