class Settings():
       """A class to store all settings for ball Invasion."""
       def __init__(self):
           """Initialize the game's settings."""
           # Screen settings
           self.screen_width = 1200
           self.screen_height = 750
           self.bg_color = (169,169,169)
           #dog Settings
           self.dog_speed_factor = 6

           # ball settings
           self.ball_speed_factor = 1
           self.ball_drop_speed = 2
