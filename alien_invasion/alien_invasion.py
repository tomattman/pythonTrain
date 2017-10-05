import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """init game, create screen object"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #set Background color
    bg_color = (ai_settings.bg_color)

    #create Ship
    ship = Ship(screen, ai_settings)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
