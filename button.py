import pygame


class Button:
    # button按钮类
    def __init__(self, style, screen):
        """初始化button按钮,分别传入按钮的初始化信息"""
        self.style = style
        self.font = pygame.font.SysFont(None, style['font_size'])
        # 获得屏幕信息
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 创建按钮矩形
        self.rect = pygame.Rect(0, 0, style['width'], style['height'])
        self.rect.centerx = self.style['x_pos']
        self.rect.centery = self.style['y_pos']
        # 返回一个surface对象
        self.msg_image = self.font.render(style['bg_word'], True, style['font_color'], style['bg_color'])
        self.image_rect = self.msg_image.get_rect()
        self.image_rect.center = self.rect.center

    def button_draw(self):
        """绘制button"""
        self.screen.fill(self.style['bg_color'], self.rect)
        # pygame.draw.rect(self.screen, self.style['bg_color'], self.rect)
        self.screen.blit(self.msg_image, self.image_rect)

