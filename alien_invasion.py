import pygame
import game_functions as gf


from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')
    ship = Ship(screen, ai_settings)
    # Создание группы для хранения пуль.
    bullets = Group()
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, aliens)
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        # Обновление дисплея
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


#Инте
run_game()
