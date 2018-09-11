import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        # 创建一个新矩形 在0,0处
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_high)
        # 重新定位
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        # 设置背景颜色
        self.color = ai_setting.bullet_color
        self.y = float(self.rect.y)
        self.bullet_speed = ai_setting.bullet_speed
        # 子弹数量
        self.bullet_allow_number = ai_setting.bullet_allow_number

    def draw_bullet(self, bullets):
        """绘制子弹"""
        self.update(bullets)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self, bullets):
        """控制子弹向上移动，碰到顶端则移除"""
        self.y -= self.bullet_speed
        self.rect.top = self.y
        # 此时到达顶端,则移除子弹
        if self.rect.top < 0:
            bullets.remove(self)






