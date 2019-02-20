import pygame

class Ship():
    
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_ret = screen.get_rect()

        self.rect.centerx = self.screen_ret.centerx
        self.rect.bottom = self.screen_ret.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        #Draft the ship in actual position
        self.screen.blit(self.image, self.rect) 

    def update(self):
        """Update the center from ship and dont the center from rectangle
        because the rectangle dont accept float data"""
        if self.moving_right and self.rect.right < self.screen_ret.right:
            self.center += self.config.ship_speed_factor
        
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.config.ship_speed_factor

        self.rect.centerx = self.center

