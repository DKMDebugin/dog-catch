import sys
import pygame
from random import randint

from ball import Ball

def check_events(dc_settings, screen, dog):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the quit event is triggered
            sys.exit() # exit game
        elif event.type == pygame.KEYDOWN: #When key is pressed
            check_keydown_events(event, dc_settings, screen, dog)
        elif event.type == pygame.KEYUP: #When key is released
            check_keyup_events(event, dog)

def check_keydown_events(event, dc_settings, screen, dog):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        dog.moving_right = True
    elif event.key == pygame.K_LEFT:
        dog.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, dog):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        dog.moving_right = False
    elif event.key == pygame.K_LEFT:
        dog.moving_left = False

def create_ball(screen, dc_settings, ballx):
    """Create a ball"""
    ball = Ball(dc_settings, screen)
    # Position the ball
    #randomly choose the x-position of the ball
    ball_width = ball.rect.width
    ball_sub_screen_width = dc_settings.screen_width - ball_width
    ball.rect.x = randint(ball_width, ball_sub_screen_width)
    ball.rect.y = ball.rect.height # Start each new ball at the top of the screen.
    ballx.add(ball)

def create_ballx(dc_settings, screen, ballx):
    """Create balllx."""
    ball = Ball(dc_settings, screen)
    number_ball_x = 1
    for ball_x in range(number_ball_x):
        create_ball(screen, dc_settings, ballx)

def check_ball_bottom(screen, dc_settings, ballx, dog):
    """check if ball is at the bottom, del & creae another"""
    for ball in ballx.sprites():
        if ball.check_bottom(dc_settings):
            ball.del_ball(ballx)
            create_ball(screen, dc_settings, ballx)
            break
        if ball.check_ball_dog_collision(dog):
            ball.del_ball(ballx)
            create_ball(screen, dc_settings, ballx)


def update_balls(screen, dc_settings, ballx, dog):
    """
    Check if the ball is at the bottom,
    Update the postions of  ball in the fleet.
    """
    check_ball_bottom(screen, dc_settings, ballx, dog, )
    ballx.update(dc_settings)

def update_screen(dc_settings, screen, dog, ballx):
    """Update images on the screen and flip to the new screen."""
    screen.fill(dc_settings.bg_color) #Redraw the screen during each pass through the loop.
    dog.blitme() #Redraw dog at its current location
    ballx.draw(screen) #Redraw each ball in the group to the screen
    pygame.display.flip() # Make the most recently drawn screen visible.
