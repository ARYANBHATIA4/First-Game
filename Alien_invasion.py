#import sys shifted to game function as is only required while calling events regarding exiting ect
import pygame
#imports Settings class from settings.py file
from settings import Settings
#imports Ship class from ship.py file 
from ship import Ship

import game_functions as gf 
#importing Group from sprite
from pygame.sprite import Group

def run_game():
    #initialises game and create screen objects
    pygame.init()
    #calling class in ai_settings
    ai_settings = Settings()
    #makes screen of specific dimensions
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #caption of screen   
    pygame.display.set_caption("RunLien")    
    #makes an instance of ship
    ship = Ship(ai_settings, screen)
    #group to store bullets in it
    bullets = Group()
    aliens = Group()
    #creates fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #start main looop of the game
    #any action taken by the user is taken here (in a game things tent to change alot therfore while things are changing screen gets updated)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens) 
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

#function run
run_game()


