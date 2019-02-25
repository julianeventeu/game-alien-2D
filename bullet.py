import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
        Class manager bullets from ship
    """

    def __init__(self, config, screen, ship):
        #super(Bullet,self).__init__() [PYTHON 2.7]
        super().__init__()
        self.screen = screen


        self.rect = pygame.Rect(0, 0, config.bullet_width, config.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #keep the bullet position like a decimal value
        self.y = float(self.rect.y)

        self.color = config.bullet_color
        self.speed_factor = config.bullet_speed_factor

    def update(self):
        #move the bullet to top
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
