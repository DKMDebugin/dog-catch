import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    '''initialize background picture'''
    def __init__(self):
        super().__init__()
        # Load the ball image and set its rect attribute.
        self.image = pygame.image.load('images/grass.bmp')
        self.rect = self.image.get_rect()
        # position image
        self.rect.left = 0
        self.rect.top = 0
