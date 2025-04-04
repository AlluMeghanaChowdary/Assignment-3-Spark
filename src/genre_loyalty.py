import pandas as pd
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Load datasets
logs = pd.read_csv("input/listening_logs.csv")
songs = pd.read_csv("input/songs_metadata.csv")

print("✅ Logs loaded:", logs.shape)
print("✅ Songs metadata loaded:", songs.shape)

# Merge listening logs with song metadata
data = logs.merge(songs, on="song_id")

# Total plays per user
total_plays = data.groupby('user_id').size()

# Genre play counts per user
genre_plays = data.groupby(['user_id', 'genre']).size().reset_index(name='plays')

# Find each user's top genre by play count
top_genre = genre_plays.sort_values(['user_id', 'plays'], ascending=[True, False]) \
                       .groupby('user_id') \
                       .first() \
                       .reset_index()

# Calculate loyalty score: top genre plays / total plays
top_genre['loyalty_score'] = top_genre.apply(
    lambda row: row['plays'] / total_plays[row['user_id']],
    axis=1
)

# Filter users with loyalty score > 0.8
loyal_users = top_genre[top_genre['loyalty_score'] > 0.5]

# Save result
output_path = "output/genre_loyalty.csv"
loyal_users.to_csv(output_path, index=False)

print("✅ Genre loyalty analysis complete.")
print("🎯 Users with loyalty score > 0.8:", len(loyal_users))
print(loyal_users.head())