#quits the game when user wants to
import sys

import pygame

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = False
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False
#above and below functions are called in check event for convinence 
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = True
    elif event.key == pygame.K_LEFT:
                ship.moving_left = True

#records keyboard and mouse events
def check_events(ship):
    #checks for events in pygame lib    
    for event in pygame.event.get():
        #compares that event with QUIT event
        if event.type == pygame.QUIT:
            #exits the game when encountered
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship):
    #ship is placed on screen after the screen is filled with colours
    screen.fill(ai_settings.bg_color)
    #make most recently drawn screen visible
    ship.blitme()
    pygame.display.flip()