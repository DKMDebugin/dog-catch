import sys
import pygame

from  dog import Dog
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

def create_ball(dc_settings, screen, ball):
    """Create an ball and place it in the row."""
    ball = ball(dc_settings, screen)
    ball_width = ball.rect.width
    ball.rect.x = randint(ball_width, dc_settings.screen_width - ball_width)
    ball.rect.top = screen.rect.top
    balls.add(ball)

def change_ball_direction(dc_settings, ball):
    """Drop the ball"""
    ball.rect.y += dc_settings.ball_drop_speed


def update_balls(dc_settings, dog, ball):
    """
    Check if the fleet is at an edge,
    Update the postions of all balls in the fleet.
    """
    change_ball_direction(dc_settings, ball)
    ball.update(dc_settings)

    # collisions = pygame.sprite.groupcollide(bullets, balls, True, True)
    # create_fleet(ai_settings, screen, ship, balls)

def update_screen(dc_settings, screen, dog, ball):
    """Update images on the screen and flip to the new screen."""

    screen.fill(dc_settings.bg_color) #Redraw the screen during each pass through the loop.

    dog.blitme() #Redraw dog at its current location
    ball.blitme() #Redraw each ball in the group to the screen
    pygame.display.flip() # Make the most recently drawn screen visible.
