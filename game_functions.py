import sys

import pygame

from bullet import Bullet

from alien import Alien


def check_event(ship, bullets, screen, ai_settings):
    """监视此时的事件"""
    # 每当用户按键时，都在pygame中注册一个事件。事件都是通过方法pygame.event.get()获取的
    for event in pygame.event.get():
        # 关闭事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 键盘按压事件
        elif event.type == pygame.KEYDOWN:
            key_down_event(event, ship, bullets, ai_settings, screen)
        # 键盘抬起事件
        elif event.type == pygame.KEYUP:
            key_up_event(event, ship)


def update_screen(ai_settings, ship, screen, bullets, aliens):
    """更新屏幕"""
    # 填充背景颜色
    # 为屏幕显示对象填充颜色 fill方法只有一个参数，即为RGB形式的元组对象
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人舰队
    for alien in aliens:
        alien.draw_alien(aliens, bullets, ship)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet(bullets)
    # 更新飞船位置
    ship.update_pos()
    # 刷新屏幕
    # 让最近绘制的屏幕可见，达到刷新屏幕的效果
    pygame.display.flip()


def key_down_event(event, ship, bullets, ai_setting, screen):
    """键盘按压事件"""
    if event.key == pygame.K_RIGHT:
        ship_key_right(ship)
    elif event.key == pygame.K_LEFT:
        ship_key_left(ship)
    elif event.key == pygame.K_UP:
        ship_key_up(ship)
    elif event.key == pygame.K_DOWN:
        ship_key_down(ship)
    elif event.key == pygame.K_SPACE:
        # 按下空格键，则发射子弹
        fire_bullet(ship, bullets, screen, ai_setting)
    elif event.key == pygame.K_q:
        sys.exit()


def key_up_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.continue_right = False
    elif event.key == pygame.K_LEFT:
        ship.continue_left = False
    elif event.key == pygame.K_UP:
        ship.continue_up = False
    elif event.key == pygame.K_DOWN:
        ship.continue_down = False


def ship_key_right(ship):
    """键盘右键的点击事件"""
    ship.continue_right = True


def ship_key_left(ship):
    """键盘左键的点击事件"""
    ship.continue_left = True


def ship_key_up(ship):
    """键盘上键的点击事件"""
    ship.continue_up = True


def ship_key_down(ship):
    """键盘下键的点击事件"""
    ship.continue_down = True


def fire_bullet(ship, bullets, screen, ai_setting):
    """键盘的space按压事件，代表子弹发射"""
    # 如果子弹数量超过设定值，则不创建
    if len(bullets) < ai_setting.bullet_allow_number:
        the_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(the_bullet)
    else:
        pass



