import pygame
#sprite helps in grouping related elements
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets"""
    def __init__(self, ai_settings, screen, ship):
        """creates a bullet object at ships current position"""
        super(Bullet, self).__init__()
        self.screen = screen
        #create a bullet at 0,0 and set its current positon
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        #center the bullet coordinates and match the bullet and ships top
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #store value in float for convinience
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """moving bullet up the screen"""
        #update the decimal position of the bullet 
        self.y -= self.speed_factor
        #as y is constantly decreasing
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)