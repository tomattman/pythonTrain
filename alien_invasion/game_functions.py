import pygame

import sys

def check_events(ship):
    """Отслеживание событий клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Обновляет изображение на экране и отображает новый экран"""
    #Перерисовывание экрана каждый раз
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Отслеживание последнего прорисованного экрана
    pygame.display.flip()
