import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """This class represents single fleet of aliens"""
    def __init__(self, ai_settings, screen):
        """initialize the alien and set its position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #start each new alien to the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draws alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """returns true when alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        #alien to the right of screen
        if self.rect.right >= screen_rect.right:
            return True
        #alien to the left of screen
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        """moving aliens right or left"""
        
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x