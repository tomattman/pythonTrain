
class Settings():
    """Store game settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        #ship settings
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 0.3
        self.bullet_speed_factor = 3
        self.alien_points = 50
        #flet_direction = 1 - right; -1 - left
        self.flet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
