import pygame 
from pygame.locals import *

from settings import Settings
from ship import Ship
import game_function as gameAux

def run_game():
    
    pygame.init()
    config = Settings()    

    screen = pygame.display.set_mode((config.screen_width,config.screen_height))
    pygame.display.set_caption("Alien Invasion")    
    
    ship = Ship(screen)    

    while True:
        gameAux.check_events(ship)
        ship.update()
        gameAux.udpdate_screen(config, screen, ship)
        

run_game()