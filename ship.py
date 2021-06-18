import pygame

class Ship():
    def __init__(self, screen):
        """initialize ship and set starting position"""
        self.screen  = screen
        
        #load image and get its rect;
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()   #rect == rectangle pygame treates its objects as rectangles
        self.screen_rect = screen.get_rect()

        #positioning ship to bottom centre of screen
        self.rect.centerx = self.screen_rect.centerx    #centers from x axis
        self.rect.bottom = self.screen_rect.bottom      #centers from y axis

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
