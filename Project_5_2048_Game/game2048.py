import json
import os
import random

class Game2048:
    def __init__(self, difficulty=1):
        self.size = 4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.difficulty = difficulty
        self.undo_stack = []
        self.add_new_tile()
        self.add_new_tile()

    def initialize_leaderboard_file(self, filename='leaderboard.json'):
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

    def save_leaderboard(self, name):
        leaderboard_file = 'leaderboard.json'
        self.initialize_leaderboard_file(leaderboard_file)  # Ensure the file is properly initialized

        try:
            with open(leaderboard_file, 'r') as f:
                try:
                    leaderboard = json.load(f)
                except json.JSONDecodeError:
                    print("Error: Leaderboard file is corrupted. Resetting to empty.")
                    leaderboard = []
        except IOError as e:
            print(f"Error reading leaderboard file: {e}")
            leaderboard = []

        leaderboard.append({"name": name, "score": self.score})
        leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:10]  # Top 10

        try:
            with open(leaderboard_file, 'w') as f:
                json.dump(leaderboard, f, indent=4)
            print(f"Leaderboard saved: {leaderboard}")
        except IOError as e:
            print(f"Error writing to leaderboard file: {e}")

    def save_state(self):
        self.undo_stack.append((self.copy_board(), self.score))

    def copy_board(self):
        return [row[:] for row in self.board]

    def add_new_tile(self):
        empty_tiles = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.board[r][c] = 4 if random.random() > 0.9 else 2

    def move_up(self):
        self.save_state()
        self.board = [list(row) for row in zip(*self.board)]  # Transpose
        self.move_left()
        self.board = [list(row) for row in zip(*self.board)]  # Transpose back

    def move_down(self):
        self.save_state()
        self.board = [list(row) for row in zip(*self.board)]  # Transpose
        self.move_right()
        self.board = [list(row) for row in zip(*self.board)]  # Transpose back

    def move_left(self):
        self.save_state()
        moved = False
        for r in range(self.size):
            row = self.board[r]
            new_row = [0] * self.size
            last_index = -1
            for c in range(self.size):
                if row[c] != 0:
                    if last_index != -1 and new_row[last_index] == row[c]:
                        new_row[last_index] *= 2
                        self.score += new_row[last_index]
                        moved = True
                    else:
                        last_index += 1
                        new_row[last_index] = row[c]
                        moved = moved or (c != last_index)
            self.board[r] = new_row

        if moved:
            self.add_new_tile()

    def move_right(self):
        self.save_state()
        for r in range(self.size):
            row = self.board[r][::-1]
            new_row = [0] * self.size
            last_index = -1
            for c in range(self.size):
                if row[c] != 0:
                    if last_index != -1 and new_row[last_index] == row[c]:
                        new_row[last_index] *= 2
                        self.score += new_row[last_index]
                    else:
                        last_index += 1
                        new_row[last_index] = row[c]
            self.board[r] = new_row[::-1]

    def can_move(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return True
                if c < self.size - 1 and self.board[r][c] == self.board[r][c + 1]:
                    return True
                if r < self.size - 1 and self.board[r][c] == self.board[r + 1][c]:
                    return True
        return False

    def undo(self):
        if self.undo_stack:
            self.board, self.score = self.undo_stack.pop()
        else:
            print("No moves to undo.")
            