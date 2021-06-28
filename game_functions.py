#quits the game when user wants to
import sys

import pygame

from bullet import Bullet

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = False
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False
#above and below functions are called in check event for convinence 
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

#records keyboard and mouse events
def check_events(ai_settings, screen, ship, bullets):
    #checks for events in pygame lib    
    for event in pygame.event.get():
        #compares that event with QUIT event
        if event.type == pygame.QUIT:
            #exits the game when encountered
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship, alien, bullets):
    #ship is placed on screen after the screen is filled with colours
    screen.fill(ai_settings.bg_color)
    #redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #make most recently drawn screen visible
    ship.blitme()
    alien.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    #getting rid of the old bullets
    # we should not remove anything directly from group so .copy()    
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    #create a new bullet and add it in group
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    