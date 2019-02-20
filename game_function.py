import sys

import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #check if the key was pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        #check if the key was release
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:                
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def udpdate_screen(config, screen, ship):
    """ Update the images on screen and show the new screen"""
    screen.fill(config.bg_color)
    ship.blitme()

    #show the last screen
    pygame.display.flip()