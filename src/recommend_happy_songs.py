import pandas as pd
import os

os.makedirs("output", exist_ok=True)

logs = pd.read_csv("input/listening_logs.csv")
songs = pd.read_csv("input/songs_metadata.csv")
data = logs.merge(songs, on="song_id")

user_genre_counts = data.groupby(['user_id', 'mood']).size().unstack(fill_value=0)
sad_dominant_users = user_genre_counts[user_genre_counts['Sad'] > user_genre_counts.max(axis=1) * 0.5].index

happy_songs = songs[songs['mood'] == 'Happy']
recommendations = []

for user in sad_dominant_users:
    played = data[data['user_id'] == user]['song_id'].unique()
    recs = happy_songs[~happy_songs['song_id'].isin(played)].head(3)
    for _, row in recs.iterrows():
        recommendations.append([user, row['song_id'], row['title']])

rec_df = pd.DataFrame(recommendations, columns=['user_id', 'song_id', 'title'])
rec_df.to_csv("output/happy_recommendations.csv", index=False)