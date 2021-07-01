#seprate file for settings as it would be changed alot
#class name with first letter capital
class Settings():
    """class to store all the settings of Alien Invasion"""
    def __init__(self):
        """initialize game settings"""
        #screen settings
        self.screen_width = 1299
        #blank screen of 1200 x 800 dimension 
        self.screen_height = 800
        #bgcolor in RGB
        self.bg_color = (164,218,244)    
        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed_factor = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 16
        #1=right -1=left
        self.fleet_direction = 1