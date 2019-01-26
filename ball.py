import pygame
from pygame.sprite import Sprite

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
       # Start each new ball near the top left of the screen.
       self.rect.x = self.rect.width
       self.rect.y = self.rect.height
       # Store the ball's exact position.
       self.y = float(self.rect.y)


    def update(self, dc_settings):
        """Move the ball down"""
        self.y += dc_settings.ball_drop_speed
        self.rect.y = self.y

    def blitme(self):
       """Draw the ball at its current location."""
       self.screen.blit(self.image, self.rect)
