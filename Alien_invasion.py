import sys  #quits the game when user wants to

import pygame

from settings import Settings 

from ship import Ship

def run_game():
    #initialises game and create screen objects
    pygame.init()
    ai_settings = Settings()   #calling class in ai_settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   
    pygame.display.set_caption("Alien invasion")    #caption of screen

    ship = Ship(screen)  #makes an instance of ship

    #start main looop of the game
    while True:     #any action taken by the user is taken here (in a game things tent to change alot therfore while things are changing screen gets updated)
        #records keyboard and mouse events
        for event in pygame.event.get():    #checks for events in pygame lib
            if event.type == pygame.QUIT:   #compares that event with QUIT event
                sys.exit()  #exits the game when encountered 
        screen.fill(ai_settings.bg_color) #fills the screen with this color
        #ship is placed on screen after the screen is filled with colours
        ship.blitme()

        #make most recently drawn screen visible
        pygame.display.flip()

run_game() #function run


