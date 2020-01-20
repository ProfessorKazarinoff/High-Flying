# settings.py
"""
File for the settings used in the Arcade game
"""

import arcade

# Screen Properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plane Flying Game with Arcade and Python"

# Scaling
SCALING = 2.0
SPRITE_SCALING_COIN = 0.25

# Movement
MOVEMENT_SPEED = 5

# Shape Properties
RADIUS = 150

# Colors
BACKGROUND_COLOR = arcade.csscolor.LIGHT_SKY_BLUE
CIRCLE_COLOR = arcade.color.BLUE

# Coins
COIN_COUNT = 50
COIN_SPRITE_IMAGE = ":resources:images/items/coinGold_ul.png"
COIN_SPRITE_SCALING = 0.4
COIN_SPEED = 4

# Bombs
BOMB_COUNT = 10
BOMB_SPRITE_IMAGE = ":resources:images/enemies/saw.png"
# ":resources:images/enemies/bee.png"
# images/bomb.png
BOMB_SPRITE_SCALING = 0.50
BOMB_SPEED = 2

# Score
SCORE_FONT_SIZE = 14
SCORE_FONT_COLOR = arcade.color.WHITE_SMOKE

# Lucy x5
PLAYER_SPRITE_IMAGE = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk4.png"
SPRITE_SCALING_PLAYER = 0.5

# Score and damage
DAMAGE_START_POINTS = 3
