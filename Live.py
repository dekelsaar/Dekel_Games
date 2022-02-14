import GuessGame
import MemoryGame
import CurrencyRouletteGame
global chosen_difficulty, chosen_game


def welcome():
    name = input("# Please enter your name ")
    print(f"Hello {name} and welcome to the world of games. Here you can find cool games to play: ")


def load_game():
    print("\n# Please choose a game to play:"
          "\n    1: Memory Game - a sequence of numbers will appear for 1 second and you have to "
          "guess it back "
          "\n    2: Guess Game - guess a number and see if you choose like the computer"
          "\n    3: Currency Roulette - try and guess the value of a random amount of USD in NIS\n")

    while True:
        try:
            chosen_game = int(input("Please choose a game to play, enter a number from 1 to 3: "))
            while 3 < chosen_game or chosen_game < 1:
                chosen_game = int(input("Please enter a number from 1 to 3: "))
            chosen_difficulty = int(input('Please choose game difficulty from 1 to 5:'))
            while 5 < chosen_difficulty or chosen_difficulty < 1:
                chosen_difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        except ValueError:
            print("Invalid chars please try again")
        if chosen_game == 1:
            MemoryGame.play(chosen_difficulty)

        if chosen_game == 2:
            GuessGame.play(chosen_difficulty)

        if chosen_game == 3:
            CurrencyRouletteGame.play(chosen_difficulty)
        return chosen_difficulty, chosen_game


