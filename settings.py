#seprate file for settings as it would be changed alot
class Settings():#class name with first letter capital
    """class to store all the settings of Alien Invasion"""
    def __init__(self):
        """initialize game settings"""
        #screen settings
        self.screen_width = 1200        #blank screen of 1200 x 800 dimension
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     #bgcolor in RGB
