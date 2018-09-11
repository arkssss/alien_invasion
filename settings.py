# 设置类
class Setting:

    def __init__(self):
        self.screen_width = 1200
        self.screen_high = 800
        # 屏幕大小
        self.screen_large = (self.screen_width, self.screen_high)
        # 背景颜色
        self.bg_color = (230, 230, 230)
        # 标题
        self.caption = "Alien_Invasion"
        # 飞船速度
        self.ship_speed = 3
        # 关于子弹
        self.bullet_width = 100
        self.bullet_high = 10
        self.bullet_color = (90, 90, 90)
        self.bullet_speed = 3
        self.bullet_allow_number = 3
        # 关于外星飞船
        self.alien_x_speed = 3
        self.alien_y_speed = 0.5
        self.alien_allow_number = 40
        # 关于游戏模式
        self.game_mode = 2
