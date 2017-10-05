import pygame

import sys
from bullet import Bullet
from alien import Alien
from ship import Ship
from time import sleep
from game_stats import GameStats

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
                fire_bullet(ai_settings, screen, ship, bullets)

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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_n:
        stats.reset_stats()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        stats.level += 1
        sb.prep_level()
        ship.center_ship()
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.flet_direction *= -1

def create_fleet(ai_settings, screen, ship, aliens):
    """create aliens fleet"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_number_aliens(ai_settings, alien_width)
    number_aliens_y = get_number_row(ai_settings, ship.rect.height, alien_height)

    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            aliens.add(create_alien(ai_settings, screen, aliens, alien_number, row_number))

def get_number_aliens(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))

def get_number_row(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 3 * alien_height - ship_height)
    return int(available_space_y / (2 * alien_height))

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y

    return alien

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Обновляет изображение на экране и отображает новый экран"""
    #Перерисовывание экрана каждый раз
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    sb.show_score()
    #Отслеживание последнего прорисованного экрана
    pygame.display.flip()
