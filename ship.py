import pygame


# 飞船类
class Ship:
    # screen传入为整个屏幕对象，目的是指出飞船的绘制地点
    def __init__(self, screen, ai_setting):
        """初始化飞船并设置其初试位置"""
        self.setting = ai_setting
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        # 返回一个rect对象，pygame以矩形为处理对象的的基本，如果一个图形不是矩形，则获得该图像的外接矩形
        # 获得飞船图像的外接矩形
        self.rect = self.image.get_rect()
        # 获得屏幕的外接矩形
        self.screen_rect = screen.get_rect()
        # 初始化
        self.init_pos()

    def blitme(self):
        """绘制图像"""
        # 在制定位置绘制图像
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        """处理连续按压"""
        if self.continue_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.setting.ship_speed
        elif self.continue_left and self.rect.left > 0:
            self.centerx -= self.setting.ship_speed
        elif self.continue_up and self.rect.top > 0:
            self.centery -= self.setting.ship_speed
        elif self.continue_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.setting.ship_speed
        #     更新
        self.rect.center = (self.centerx, self.centery)

    def init_pos(self):
        """初始化飞船的位置"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.centery
        # self.rect.center = self.screen_rect.center
        # rect的center属性为图像的中心点坐标，为一个元组
        # 同样centerx，centery属性为图像中心点的x,y轴的坐标
        # print(type(self.rect.center))
        # print(type(self.rect.centerx))
        # print(type(self.rect.bottom))
        # print(self.screen_rect.right)
        # 控制键盘按键持续移动的变量
        self.continue_right = False
        self.continue_left = False
        self.continue_up = False
        self.continue_down = False
        # 小数的方式更加精细的控制
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)