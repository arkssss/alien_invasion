from settings import Setting
from ship import Ship
from pygame.sprite import Group
from game_state import GameState
import pygame
import game_functions


def run_game():
    pygame.init()
    # 配置文件对象
    ai_settings = Setting()
    # 游戏运行时状态类
    state = GameState(ai_settings)
    # surface对象表示屏幕的一部分，用于显示游戏元素
    # 游戏中每一个显示对象（如飞机，子弹）都是一个surface对象
    # screen 为surface对象 ， 此时的screen表示的为整个显示的屏幕
    screen = pygame.display.set_mode(ai_settings.screen_large)
    pygame.display.set_caption(ai_settings.caption)
    # 飞船对象
    ship = Ship(screen, ai_settings)
    # 外星人飞船组
    aliens = Group()
    # 子弹对象
    bullets = Group()
    while True:
        # 审查事件
        game_functions.check_event(ship, bullets, screen, ai_settings)
        # 绘制屏幕
        game_functions.update_screen(ai_settings, ship, screen, bullets, aliens, state)


run_game()

