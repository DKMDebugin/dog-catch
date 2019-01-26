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
    pygame.display.set_caption("Dog Catch")


    dog = Dog(dc_settings, screen)
    ballx = Group()
    gf.create_ballx(dc_settings, screen, ballx)

    #Gmme main loop
    while True:
        gf.check_events(dc_settings, screen, dog)
        dog.update()
        gf.update_balls(screen, dc_settings, ballx, dog)
        gf.update_screen(dc_settings, screen, dog, ballx)

run_game()
