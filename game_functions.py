import sys  #quits the game when user wants to
import pygame

def check_events():      #records keyboard and mouse events
    for event in pygame.event.get():    #checks for events in pygame lib
        if event.type == pygame.QUIT:   #compares that event with QUIT event
            sys.exit()  #exits the game when encountered 

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color) #fills the screen with this color
        #ship is placed on screen after the screen is filled with colours
    ship.blitme()
        #make most recently drawn screen visible
    pygame.display.flip()