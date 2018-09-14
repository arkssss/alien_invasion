from settings import Setting
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import pygame
import game_functions


def run_game():
    pygame.init()
    # 配置文件对象
    ai_settings = Setting()
    # surface对象表示屏幕的一部分，用于显示游戏元素
    # 游戏中每一个显示对象（如飞机，子弹）都是一个surface对象
    # screen 为surface对象 ， 此时的screen表示的为整个显示的屏幕
    screen = pygame.display.set_mode(ai_settings.screen_large)
    pygame.display.set_caption(ai_settings.caption)
    # 飞船对象
    ship = Ship(screen, ai_settings)
    # 外星人飞船组
    aliens = Group()
    Alien.init_aliens_group(aliens, ai_settings, screen)
    # while len(aliens) < ai_settings.alien_allow_number:
    #     alien = Alien(ai_settings, screen, aliens)
    #     aliens.add(alien)
    # 子弹对象
    bullets = Group()
    while True:
        # 审查事件
        game_functions.check_event(ship, bullets, screen, ai_settings)
        # 绘制屏幕
        game_functions.update_screen(ai_settings, ship, screen, bullets, aliens)


run_game()

