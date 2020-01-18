# window.py
"""
A module which contains the custom arcade Window class
"""

import random
import arcade
import os
from sprites import Player, Coin, LeftMovingCoin, Bomb
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    BACKGROUND_COLOR,
    MOVEMENT_SPEED,
    SPRITE_SCALING_PLAYER,
    SPRITE_SCALING_COIN,
    COIN_COUNT,
    BOMB_COUNT,
    SCORE_FONT_SIZE,
    SCORE_FONT_COLOR,
)

# Custom Window Class
class SpaceGame(arcade.Window):
    """The main window which appears then the game is run"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.player_sprite = None
        self.coin_list = None
        self.enemies_list = arcade.SpriteList
        self.clouds_list = arcade.SpriteList
        self.all_sprites = arcade.SpriteList

        self.score = 0

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """Get game ready to play"""

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = Player(
            ":resources:images/space_shooter/playerShip1_orange.png",
            SPRITE_SCALING_PLAYER,
        )
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            coin = LeftMovingCoin(
                ":resources:images/items/coinGold_ul.png", SPRITE_SCALING_COIN
            )
            # position of each coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            # add coin to coin list
            self.coin_list.append(coin)

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        # put the score on the screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 20, SCORE_FONT_COLOR, SCORE_FONT_SIZE)

    def on_update(self, delta_time: float):
        """Movement and game logic"""
        self.coin_list.update()
        self.player_list.update()
        # list of all the sprites the collided with the player
        coins_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )
        # Look through each colliding sprite, remove colliding sprite, add 1 to the score
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed"""
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when a key is released"""
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
