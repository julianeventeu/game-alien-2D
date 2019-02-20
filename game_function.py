import sys

import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)

        if event.type == pygame.KEYUP:     
            check_keyup_events(event,ship)             

def check_keyup_events(event,ship):
    #check if the key was release
    if event.key == pygame.K_RIGHT:                
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(event,ship):
    #check if the key was pressed
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def udpdate_screen(config, screen, ship):
    """ Update the images on screen and show the new screen"""
    screen.fill(config.bg_color)
    ship.blitme()

    #show the last screen
    pygame.display.flip()