import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        """Init Ship And setup start position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #new ships star in the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        #флаг перемещения вправо
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """update ship position"""
        if self.moving_right:
            self.move_right()
        elif self.moving_left:
            self.move_left()

    def move_right(self):
        self.change_position_x(self.ai_settings.ship_speed_factor)
    def move_left(self):
        self.change_position_x(-self.ai_settings.ship_speed_factor)
    def change_position_x(self, x):
        if 0 < self.rect.left + x and self.rect.right + x < self.ai_settings.screen_width:
             self.center += x
        self.rect.centerx = self.center
