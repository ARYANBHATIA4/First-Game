#quits the game when user wants to
import sys

from time import sleep

import pygame

from bullet import Bullet

from alien import Alien

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
#above and below functions are called in check event for convinence 
def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    #create a new bullet and add it in group
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
#records keyboard and mouse events
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    #checks for events in pygame lib    
    for event in pygame.event.get():
        #compares that event with QUIT event
        if event.type == pygame.QUIT:
            #exits the game when encountered
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """starts new game when button is clicked"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        #hiding mouse cursor
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    #ship is placed on screen after the screen is filled with colours
    screen.fill(ai_settings.bg_color)
    #redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #make most recently drawn screen visible
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    #draws a button if game is inactive 
    if not stats.game_active:
        play_button.draw_button()
    #most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #getting rid of the old bullets
    #we should not remove anything directly from group so .copy()
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #first true tells that after the bullet hits the alien bullet dissapears second T for alien
    colissions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if colissions:
        for aliens in colissions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        #destroy existing bullets, speed up and if entire fleet destroyed create a new level
        bullets.empty()
        ai_settings.increase_speed()
        #inc level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    #creates and finds no of aliens in a row
    #spacing between aliens is an alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #create an alien and place it in row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    check if the fleet is at an edge,
    and then position of all aliens in the fleet
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #checks ship and alien collision
    #takes 2 argument sprite and a group and checks collision among them sprite or none is returned
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """responds appropriately if aliens touch edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """drop the entire fleet and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """respond when collision occur"""
    if stats.ships_left > 0:
        #decrement the value of ships_left
        stats.ships_left -= 1
        #update scoreboard
        sb.prep_ships()
        #when hit remove bullets and aliens from screen
        aliens.empty()
        bullets.empty()
        #create a new fleet with ship at centre
        create_fleet(ai_settings, screen,ship, aliens)
        ship.center_ship()
        #pause for a sec to collect defeat
        sleep(1.0)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """checks for any alies reaching bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #same thin happens as it happens when ship hits alien
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def get_number_aliens_x(ai_settings, alien_width):
    """how many alien fits in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """find number of rows that could fit in the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x  = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_high_score(stats, sb):
    """check for any new highscore"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()