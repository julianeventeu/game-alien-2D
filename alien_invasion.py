import pygame 
from pygame.locals import *
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gameAux

def run_game():
    
    pygame.init()
    config = Settings()    

    screen = pygame.display.set_mode((config.screen_width,config.screen_height))
    pygame.display.set_caption("Alien Invasion")    
    
    ship = Ship(screen, config)
    bullets = Group()    

    while True:
        gameAux.check_events(ship, config, screen, bullets)
        ship.update()
        
        gameAux.update_bullets(bullets)
        gameAux.udpdate_screen(config, screen, ship,bullets)

run_game()