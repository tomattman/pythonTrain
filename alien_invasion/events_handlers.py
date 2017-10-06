import pygame
import sys

import game_functions as gf

def check_events(ai_settings, stats, sb, screen, ship, bullets, play_button):
    """Отслеживание событий клавиатуры и мыши"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not stats.game_active:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button, mouse_x, mouse_y)
            else:
                gf.fire_bullet(ai_settings, screen, ship, bullets)

def check_play_button(ai_settings, screen, stats, sb, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        sb.prep_score()
        sb.prep_level()
        stats.game_active = True
        pygame.mouse.set_visible(False)
        sb.prep_ships()

def check_keydown_events(event, ai_settings, stats, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        gf.fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_n:
        stats.reset_stats()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
