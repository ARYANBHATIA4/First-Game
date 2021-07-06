class GameStats():
    """tracks statistics for RunLien"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #start RunLien in an Inactive state
        self.game_active = False
        #highscore NOT in reset
        self.high_score = 0

    def reset_stats(self):
        """initializes text that is changes during the game proceding"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1