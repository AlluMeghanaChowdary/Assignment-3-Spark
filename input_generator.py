import os
import csv
import random
from datetime import datetime, timedelta

# Create input folder if it doesn't exist
os.makedirs("input", exist_ok=True)

# Constants
NUM_USERS = 50
NUM_SONGS = 100
NUM_LOGS = 3000
GENRES = ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip-Hop']
MOODS = ['Happy', 'Sad', 'Energetic', 'Chill']

# Generate songs_metadata.csv
song_metadata = []
for i in range(1, NUM_SONGS + 1):
    song_metadata.append([
        f"S{i:04}",                             # song_id
        f"Song Title {i}",                      # title
        f"Artist {random.randint(1, 50)}",      # artist
        random.choice(GENRES),                 # genre
        random.choice(MOODS)                   # mood
    ])

with open("input/songs_metadata.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["song_id", "title", "artist", "genre", "mood"])
    writer.writerows(song_metadata)

# Load the generated Pop songs for loyalty simulation
pop_song_ids = [row[0] for row in song_metadata if row[3] == 'Pop']

# Generate listening_logs.csv
start_date = datetime(2025, 3, 17)
end_date = datetime(2025, 3, 30)
seconds_in_range = int((end_date - start_date).total_seconds())

listening_logs = []
for _ in range(NUM_LOGS):
    user_id_num = random.randint(1, NUM_USERS)
    user_id = f"U{user_id_num:03}"

    # First 10 users will mostly play Pop songs
    if user_id_num <= 10 and random.random() < 0.85:
        song_id = random.choice(pop_song_ids)
    else:
        song_id = f"S{random.randint(1, NUM_SONGS):04}"

    timestamp = start_date + timedelta(seconds=random.randint(0, seconds_in_range))
    duration = random.randint(30, 300)

    listening_logs.append([
        user_id,
        song_id,
        timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        duration
    ])

with open("input/listening_logs.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user_id", "song_id", "timestamp", "duration_sec"])
    writer.writerows(listening_logs)

print("✅ Datasets saved in the 'input/' folder with loyal users!")