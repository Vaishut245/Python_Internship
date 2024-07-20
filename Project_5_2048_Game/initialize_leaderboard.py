import json
import os

def initialize_leaderboard_file(filename='leaderboard.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)  # Create an empty list to start with
        print("Created an empty leaderboard file.")
    else:
        # Check if the file is empty
        if os.path.getsize(filename) == 0:
            with open(filename, 'w') as f:
                json.dump([], f)  # Reset to empty list
            print("Leaderboard file was empty. Reset to an empty list.")

initialize_leaderboard_file()
