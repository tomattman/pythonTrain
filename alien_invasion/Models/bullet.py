import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to bullet control"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #create bullet in position (0,0) and setup right position
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet by screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """print bullet on screen"""
        self.screen.blit(self.image, self.rect)
