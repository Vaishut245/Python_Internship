from game2048 import Game2048
from gui2048 import GUI2048

def main():
    game = Game2048(difficulty='normal')  # Change difficulty here
    gui = GUI2048(game)

if __name__ == "__main__":
    main()
