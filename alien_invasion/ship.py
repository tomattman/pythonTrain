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

        self.center_ship();

        #флаг перемещения вправо
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        #new ships star in the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """update ship position"""
        if self.moving_right:
            self.move_right()
        elif self.moving_left:
            self.move_left()
        if self.moving_up:
            self.move_up()
        elif self.moving_down:
            self.move_down()

    def move_right(self):
        self.change_position_x(self.ai_settings.ship_speed_factor)
    def move_left(self):
        self.change_position_x(-self.ai_settings.ship_speed_factor)
    def change_position_x(self, x):
        if 0 < self.rect.left + x and self.rect.right + x < self.ai_settings.screen_width:
             self.center_x += x
        self.rect.centerx = self.center_x

    def move_up(self):
        self.change_position_y(-self.ai_settings.ship_speed_factor)
    def move_down(self):
        self.change_position_y(self.ai_settings.ship_speed_factor)
    def change_position_y(self, y):
        if 0 < self.rect.top + y and self.rect.bottom + y < self.ai_settings.screen_height:
             self.center_y += y
        self.rect.centery = self.center_y
