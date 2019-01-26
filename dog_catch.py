import pygame
from pygame.sprite import Group

from settings import Settings
from dog import Dog
from ball import Ball
import game_function as gf

def run_game():
    '''
    Initialize pygame ,
    create a screen object
    (window screen size & window caption) & settings
    '''
    pygame.init()
    dc_settings = Settings() #Object of Settings() class
    screen = pygame.display.set_mode(
    (dc_settings.screen_width, dc_settings.screen_height)) #set screen size by passing in Settings width & height attributes
    pygame.display.set_caption("ball Invasion")

    dog = Dog(dc_settings, screen)
    ball = Ball(dc_settings, screen)

    while True:
        gf.check_events(dc_settings, screen, dog)
        dog.update()
        # gf.update_bullets(dc_settings, screen, dog, balls, bullets)
        gf.update_balls(dc_settings, dog, ball)
        gf.update_screen(dc_settings, screen, dog, ball)




run_game()
