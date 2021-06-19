#import sys shifted to game function as is only required while calling events regarding exiting ect

import pygame
from settings import Settings 
from ship import Ship
import game_functions as gf 

def run_game():
    #initialises game and create screen objects
    pygame.init()
    ai_settings = Settings()   #calling class in ai_settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   
    pygame.display.set_caption("Alien invasion")    #caption of screen

    ship = Ship(screen)  #makes an instance of ship

    #start main looop of the game
    while True:     #any action taken by the user is taken here (in a game things tent to change alot therfore while things are changing screen gets updated)
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game() #function run


