import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class represents a unique Alien """

    def __init__(self, config, screen):
        super().__init__()
        self.screen = screen
        self.config = config

        #load the image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #define the start position near left top screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save the exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw the alien
        self.screen.blit(self.image,self.rect) 