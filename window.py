# window.py
"""
A module which contains the custom arcade Window class
"""

import random
import arcade
import os
from sprites import Player, Coin, LeftMovingCoin, Bomb
from views import GameOverView, MenuView
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    BACKGROUND_COLOR,
    MOVEMENT_SPEED,
    SPRITE_SCALING_PLAYER,
    SPRITE_SCALING_COIN,
    COIN_COUNT,
    COIN_SPRITE_IMAGE,
    COIN_SPRITE_SCALING,
    BOMB_COUNT,
    SCORE_FONT_SIZE,
    SCORE_FONT_COLOR,
    PLAYER_SPRITE_IMAGE,
    BOMB_SPRITE_IMAGE,
    BOMB_SPRITE_SCALING,
    DAMAGE_START_POINTS,
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
        self.bomb_list = None
        self.all_sprites = arcade.SpriteList

        self.score = 0
        self.damage = DAMAGE_START_POINTS
        self.game_over = False

        self.menu_view = MenuView()
        self.game_over_view = GameOverView()

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """Get game ready to play"""

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = Player(
            PLAYER_SPRITE_IMAGE,
            SPRITE_SCALING_PLAYER,
        )
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            coin = LeftMovingCoin(COIN_SPRITE_IMAGE, COIN_SPRITE_SCALING)
            # position of each coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            # add coin to coin list
            self.coin_list.append(coin)

        # Create the bombs
        for i in range(BOMB_COUNT):
            bomb = Bomb(BOMB_SPRITE_IMAGE, BOMB_SPRITE_SCALING)
            # position of each bomb
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)
            # add bomb to bomb list
            self.bomb_list.append(bomb)

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bomb_list.draw()
        # put the score and damage on the screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 20, SCORE_FONT_COLOR, SCORE_FONT_SIZE)
        damage_text = f"Damage: {self.damage}"
        arcade.draw_text(damage_text, 10, 40, SCORE_FONT_COLOR, SCORE_FONT_SIZE)

    def on_update(self, delta_time: float):
        """Movement and game logic"""
        if not self.game_over:
            self.coin_list.update()
            self.bomb_list.update()
            self.player_list.update()
            # list of all the sprites the collided with the player
            coins_hit_list = arcade.check_for_collision_with_list(
                self.player_sprite, self.coin_list
            )
            # Look through each colliding sprite, remove colliding sprite, add 1 to the score
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
            bombs_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_list)
            for bomb in bombs_hit_list:
                bomb.remove_from_sprite_lists()
                self.damage -=1
                if self.damage < 1:
                    self.game_over = True
                    #self.show_view(game_over_view)

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
