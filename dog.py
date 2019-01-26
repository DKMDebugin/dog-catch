import pygame
from pygame.sprite import Sprite

class Dog(Sprite):
    '''
    Dog() helps manage most of the behaviour of the player's dog
    '''
    def __init__(self, dc_settings, screen):
        """Initialize the dog and set its starting position."""
        #initialize the parameters
        self.screen = screen
        self.dc_settings = dc_settings
        # Load the dog image and get its rect.
        self.image = pygame.image.load('images/dog.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new dog at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx #centerx attribute position game element at the top center. center & centery are other attri that can be used
        self.rect.bottom = self.screen_rect.bottom #postion game element at the bottom

        #Store a decimal value for the dogs's center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''
        Update the dog's position based on the movement flag.
        '''
        #Update the dog's center value, not the rect.
        if  self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.dc_settings.dog_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.dc_settings.dog_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the dog at its current location."""
        self.screen.blit(self.image, self.rect)
