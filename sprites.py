# sprites.py

"""Custom Sprite Class"""

import arcade

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COIN_SPEED,
    BOMB_SPEED
)

class Player(arcade.Sprite):
    """Player sprite can't move off screen"""

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT


class Coin(arcade.Sprite):
    """Coin class"""

    pass


class LeftMovingCoin(Coin):
    """A coin that moves from the right of the screen to the left"""

    def update(self):
        self.center_x -= COIN_SPEED
        if self.left < 0:
            self.left = SCREEN_WIDTH


class Bomb(arcade.Sprite):
    """Bomb class"""

    def update(self):
        self.center_x -= BOMB_SPEED
        if self.left < 0:
            self.left = SCREEN_WIDTH
