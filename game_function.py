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
        fire_bullet(ship, config, screen, bullets) 

    elif event.key == pygame.K_q:
        sys.exit()

def udpdate_screen(config, screen, ship, bullets):
    """ Update the images on screen and show the new screen"""
    screen.fill(config.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    #show the last screen
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ship, config, screen, bullets):
    if len(bullets) < config.bullet_allowed:
        new_bullet = Bullet(config, screen, ship)
        bullets.add(new_bullet)