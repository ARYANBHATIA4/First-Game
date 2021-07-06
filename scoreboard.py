import pygame.font

class Scoreboard():
    """this class holds scoring values"""

    def __init__(self, ai_settings, screen, stats):
        """initial score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #prepare initial score image
        self.prep_score()

    def prep_score(self):
        """turns score into a rendered image"""
        #round returns a decimal value but when passed a negative value it returns values closest to 100
        #also py.version 2.7 and below returns only a decimal value if using above ver you can skip int part
        rounded_score = int(round(self.stats.score, -1))
        #this line adds , between zeros 1,00,000
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        #display the score at the top right corner of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)

    