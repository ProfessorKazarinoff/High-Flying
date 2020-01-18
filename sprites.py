# sprites.py

"""Custom Sprite Class"""

import arcade
import settings

SCREEN_WIDTH = settings.SCREEN_WIDTH
SCREEN_HEIGHT = settings.SCREEN_HEIGHT


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
        self.center_x -= 2
        if self.left < 0:
            self.left = SCREEN_WIDTH


class Bomb(arcade.Sprite):
    """Bomb class"""

    pass
