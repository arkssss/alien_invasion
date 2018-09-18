import pygame


# 飞船类
class Ship:
    # screen传入为整个屏幕对象，目的是指出飞船的绘制地点
    def __init__(self, screen, ai_setting, ships, mode=0):
        """初始化飞船并设置其初试位置"""
        self.setting = ai_setting
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        # 返回一个rect对象，pygame以矩形为处理对象的的基本，如果一个图形不是矩形，则获得该图像的外接矩形
        # 获得飞船图像的外接矩形
        self.rect = self.image.get_rect()
        # 获得屏幕的外接矩形
        self.screen_rect = screen.get_rect()
        # 操作者控制的飞船初化初始化
        if not mode:
            self.init_pos()
        elif mode == 1:
            self.init_icon_ship(ships)

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

    def init_icon_ship(self, ships):
        """初始化ships显示的位置"""
        ships_len = len(ships)
        self.rect.left = ships_len * self.rect.width
        self.rect.top = self.setting.ship_icon_top

    @staticmethod
    def init_ships_group(ships, screen, ai_setting):
        """初始化飞船组"""
        while len(ships) < ai_setting.ship_allow_number:
            ship = Ship(screen, ai_setting, ships, 1)
            ship.init_icon_ship(ships)
            ships.append(ship)

    @staticmethod
    def remove_ship(current_left, ships):
        """对ships飞船组里面的飞船进行移除"""
        if len(ships) == current_left:
            pass
        else:
            remove_number = len(ships) - current_left
            while remove_number != 0:
                if len(ships):
                    ships.pop()
                    remove_number -= 1




