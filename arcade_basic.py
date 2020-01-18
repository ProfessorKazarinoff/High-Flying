# arcade_basic.py
"""
A very basic arcade window creating script. Following the tutorial at RealPython.com:
https://realpython.com/arcade-python-game-framework/

Displays a white window with a blue circle in the middle
"""

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Simple Arcade Window"
RADIUS = 150
WINDOW_COLOR = arcade.color.WHITE


# Open the Window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set window background color
arcade.set_background_color(WINDOW_COLOR)

# Clear the screen and start drawing
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
)

# Finish drawing
arcade.finish_render()

# Display the window
arcade.run()
