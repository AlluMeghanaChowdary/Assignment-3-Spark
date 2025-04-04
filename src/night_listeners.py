import pandas as pd
import os

os.makedirs("output", exist_ok=True)

logs = pd.read_csv("input/listening_logs.csv")
logs['timestamp'] = pd.to_datetime(logs['timestamp'])
logs['hour'] = logs['timestamp'].dt.hour

night_logs = logs[(logs['hour'] >= 0) & (logs['hour'] < 5)]

night_users = night_logs['user_id'].value_counts()
frequent_night_users = night_users[night_users >= 5].reset_index()
frequent_night_users.columns = ['user_id', 'night_plays']

frequent_night_users.to_csv("output/night_listeners.csv", index=False)