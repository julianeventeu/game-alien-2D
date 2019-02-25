import sys

import pygame

from bullet import Bullet

def check_events(ship, config, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,config, screen, bullets)

        if event.type == pygame.KEYUP:     
            check_keyup_events(event,ship)             

def check_keyup_events(event,ship):
    #check if the key was release
    if event.key == pygame.K_RIGHT:                
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(event, ship, config, screen, bullets):
    #check if the key was pressed
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(config, screen, ship)
        bullets.add(new_bullet)

def udpdate_screen(config, screen, ship, bullets):
    """ Update the images on screen and show the new screen"""
    screen.fill(config.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    #show the last screen
    pygame.display.flip()