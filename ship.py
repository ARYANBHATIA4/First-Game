import pygame

class Ship():
    #ai_settings to be used on update
    def __init__(self,ai_settings, screen):
        """initialize ship and set starting position"""
        self.screen  = screen
        self.ai_settings = ai_settings
        #load image and get its rect;
        self.image = pygame.image.load('images/ship.png')
        #rect = rectangle pygame treates its objects as rectangles
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #positioning ship to bottom centre of screen
        #centers from x axis
        self.rect.centerx = self.screen_rect.centerx
        #centers from y axis
        self.rect.bottom = self.screen_rect.bottom
        #rect only stores int values so:
        self.center = float(self.rect.centerx)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updating ship position according to movement flag"""
        #updating ships center value not the rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx += 1
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
