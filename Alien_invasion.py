#import sys shifted to game function as is only required while calling events regarding exiting ect...
import pygame
#imports Settings class from settings.py file
from settings import Settings
#imports Ship class from ship.py file
from game_stats import GameStats

from button import Button

from ship import Ship

import game_functions as gf
#importing Group from sprite
from pygame.sprite import Group

from scoreboard import Scoreboard

def run_game():
    #initialises game and create screen objects
    pygame.init()
    #calling class in ai_settings
    ai_settings = Settings()
    #makes screen of specific dimensions
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #caption of screen
    pygame.display.set_caption("RunLien")
    #Make a play button
    play_button = Button(ai_settings, screen, "PLAY")
    #stores game stats and create a scoreboard
    stats = GameStats(ai_settings)    
    sb = Scoreboard(ai_settings, screen, stats)
    #makes an instance(easier copy) of ship
    ship = Ship(ai_settings, screen)
    #group to store bullets in it
    bullets = Group()
    aliens = Group()
    #creates fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #start main looop of the game
    #any action taken by the user is taken here (in a game things tent to change alot therfore while things are changing screen gets updated)
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

#function run
run_game()