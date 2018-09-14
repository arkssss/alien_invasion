import pygame
import random
from time import sleep
from pygame.sprite import Sprite


# 外星飞船类继承精灵类
class Alien(Sprite):
    def __init__(self, ai_setting, screen, aliens=""):
        # 调用基类构造函数
        super().__init__()
        self.speed = ai_setting.alien_x_speed
        self.speed_y = ai_setting.alien_y_speed
        self.screen = screen
        # 飞船图像设定
        self.image = pygame.image.load('images/alien.bmp')
        self.setting = ai_setting
        # 获得图形的外接矩形
        self.rect = self.image.get_rect()
        # 获得屏幕的外接矩形
        self.screen_rect = screen.get_rect()
        # 设定初始化位置
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left
        # 保存准确位置,以矩形左上角坐标为基准
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # fly_mode -1表示左飞 1表示右飞
        self.fly_mode = 0
        # fly_increase 表示x轴方向飞行增量（可正可负）
        self.fly_increase = -1
        # fly_increase_y表示y轴方向飞行增量 (目前仅为正)
        self.fly_increase_y = -1
        print(self.screen_rect.right)
        # mode_one的初始化
        if ai_setting.game_mode == 1:
            self.init_for_mode_one(ai_setting)
        #  mode_two的初始化
        if ai_setting.game_mode == 2:
            # x.width*(x + x +1) = screen.width
            # line_numbers 则为每一行容纳的外星飞船的数量
            self.line_numbers = int((self.screen_rect.width / self.rect.width - 1) / 2)
            self.init_for_mode_two(aliens)

    def draw_alien(self, aliens, bullets, ship):
        """绘制外星人飞船"""
        self.update(aliens, bullets, ship)
        self.rect.left = self.x
        self.rect.top = self.y
        self.screen.blit(self.image, self.rect)

    def init_for_mode_one(self, ai_setting):
        """模式1的方式初始化飞船,随机显示飞船"""
        # 如果为刚创建，则随机显示外星舰队
        self.x = random.randint(self.screen_rect.left, ai_setting.screen_width - self.rect.width)
        self.y = random.randint(self.screen_rect.top, ai_setting.screen_high - self.rect.height)
        # 左右横飞 -1为左飞 1为右飞
        direction = random.randint(0, 1)
        self.fly_mode = [-1, 1][direction]
        # 飞行增量，左飞为负数，右飞为正数
        self.fly_increase = self.speed * self.fly_mode

    def update_mode_one(self, aliens, bullets):
        """模式1的数据更新"""
        # 只有水平变化，属于modeone
        self.x += self.fly_increase
        # 是否撞墙
        self.is_knock_wall()
        # 是否被击中
        self.is_hit(aliens, bullets)

    def init_for_mode_two(self, aliens):
        """第二种初始化模式"""
        current_number = len(aliens)
        # 加一个一位的偏移量
        x_pos = (current_number % self.line_numbers) + 1
        y_pos = int((current_number / self.line_numbers))
        self.x = ((2 * x_pos) - 1) * self.rect.width
        self.y = (self.rect.height + 25) * y_pos
        # 先默认向右飞
        self.fly_mode = 1
        self.fly_increase = self.speed * self.fly_mode
        self.fly_increase_y = self.speed_y

    def update_mode_two(self, aliens, bullets, ship):
        """第二种更新方式"""
        # 移动飞船
        self.x += self.fly_increase
        self.y += self.fly_increase_y
        # 是否撞到墙
        self.is_knock_wall()
        # 判断是否有子弹击中，如果有则删除子弹和飞船
        self.is_hit_and_deal(aliens, bullets)
        # 判断飞船和外星舰队是否相撞如果是，则重新开始游戏
        self.is_crash_and_deal(ship, aliens)
        # 判断飞船是否撞到底部屏幕
        self.is_crash_screen_bottom(aliens, self.screen_rect, self.screen, ship, self.setting)

    def update(self, aliens, bullets, ship):
        """更新外星飞船位置，重载的方法"""
        if self.setting.game_mode == 1:
            self.update_mode_one(aliens, bullets)
        if self.setting.game_mode == 2:
            self.update_mode_two(aliens, bullets, ship)

    def is_knock_wall(self):
        """判断飞船是否撞到了墙,如果是则翻转方向"""
        if self.x < 0 or self.x > self.screen_rect.right - self.rect.width:
            self.fly_mode = -1 if self.fly_mode == 1 else 1
            self.fly_increase = self.speed * self.fly_mode

    def is_crash_and_deal(self, ship, aliens):
        """判断飞船和外星舰队是否相撞"""
        if pygame.sprite.spritecollideany(ship, aliens):
            # 如果相撞则重新开始游戏
            self.restart_game(ship, aliens, self.setting, self.screen)

    def chose_mode_function(self, current_mode, aliens):
        """根据不同的mode选择不同的初始化方式"""
        if current_mode == 1:
            self.init_for_mode_one(self.setting)
        elif current_mode == 2:
            self.init_for_mode_two(aliens)

    @staticmethod
    def is_crash_screen_bottom(aliens, screen_rect, screen, ship, setting):
        """判断飞船是否撞到了屏幕底端"""
        for alien in aliens:
            """遍历每一个alien，检查有没有低端碰到到屏幕的底端"""
            if alien.rect.bottom > screen_rect.bottom:
                Alien.restart_game(ship, aliens, setting, screen)

    @staticmethod
    def is_hit_and_deal(aliens, bullets):
        """判断子弹是否击中了飞船"""
        # 飞船的x,y轴区域 , 子弹打中飞船
        # x_area = [self.rect.left, self.rect.right]
        # y_area = [self.rect.top, self.rect.bottom]
        # for bullet in bullets:
        #     bullet_ranges = range(bullet.rect.left, bullet.rect.left + bullet.rect.width)
        #     for the_bullet in bullet_ranges:
        #         if x_area[0] <= the_bullet <= x_area[1] and y_area[0] <= the_bullet <= y_area[1]:
        #             bullets.remove(bullet)
        #             aliens.remove(self)
        #             return True
        # return False
        # 仅需要一行代码
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            return True
        else:
            return False

    @staticmethod
    def init_aliens_group(aliens, ai_setting, screen):
        """初始化外星舰队组"""
        while len(aliens) < ai_setting.alien_allow_number:
            alien = Alien(ai_setting, screen, aliens)
            aliens.add(alien)

    @staticmethod
    def restart_game(ship, aliens, setting, screen):
        """重新启动游戏"""
        aliens.empty()
        ship.init_pos()
        Alien.init_aliens_group(aliens, setting, screen)
        sleep(0.5)
