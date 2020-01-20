# run.py

"""
main script to run the game.

From the command line

 > python run.py

"""

import arcade
from window import SpaceGame
from views import MenuView, GameOverView


def main():
    window = SpaceGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
