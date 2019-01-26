import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    """A class to represent a single ball in the fleet."""

    def __init__(self, dc_settings, screen):
       """Initialize the ball and set its starting position."""
       super().__init__()
       self.screen = screen
       self.dc_settings = dc_settings
       # Load the ball image and set its rect attribute.
       self.image = pygame.image.load('images/ball.bmp')
       self.rect = self.image.get_rect()
       # Position the ball
       #random choose the x-position of the ball
       ball_sub_screen_width = dc_settings.screen_width - self.rect.width
       self.rect.x = randint(self.rect.width, ball_sub_screen_width)
       self.rect.y = self.rect.height # Start each new ball at the top of the screen.
       # Store the ball's exact position for movement
       self.y = float(self.rect.y)

    def update(self, dc_settings):
        """Move the ball top to bottom"""
        self.y += dc_settings.ball_drop_speed
        self.rect.y = self.y

    def check_bottom(self, dc_settings):
        '''check if ball is at the bottom'''
        if self.rect.top >= dc_settings.screen_height:
            return True

    def del_ball(self, ballx):
        """Delete ball"""
        for ball_x in ballx.copy():
            ballx.remove(ball_x)

    def check_ball_dog_collision(self, dog):
        '''check colliosn btw dog and ball'''
        if self.rect.bottom == dog.rect.top:
            return True

    def blitme(self):
       """Draw the ball at its current location."""
       self.screen.blit(self.image, self.rect)
