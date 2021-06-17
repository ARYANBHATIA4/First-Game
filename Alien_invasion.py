import sys  #quits the game when user wants to

import pygame

def run_game():
    #initialises game and create screen objects
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))   #blank screen of 1200 x 800 dimension
    pygame.display.set_caption("Alien invasion")    #caption of screen

    #start main looop of the game
    while True:     #any action taken by the user is taken here
        #records keyboard and mouse events
        for event in pygame.event.get():    #checks for events in pygame lib
            if event.type == pygame.QUIT:   #compares that event with QUIT event
                sys.exit()  #exits the game when encountered 
            
        #make most recently drawn screen visible
        pygame.display.flip()

run_game()


