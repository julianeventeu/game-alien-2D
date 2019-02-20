import pygame

class Ship():
    
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_ret = screen.get_rect()

        self.rect.centerx = self.screen_ret.centerx
        self.rect.bottom = self.screen_ret.bottom

        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        #Draft the ship in actual position
        self.screen.blit(self.image, self.rect) 

    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        
        elif self.moving_left:
            self.rect.centerx -=1


