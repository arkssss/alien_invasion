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
        self.ship_speed = 10
        self.ship_allow_number = 3
        # 关于子弹
        self.bullet_width = 1200
        self.bullet_high = 10
        self.bullet_color = (90, 90, 90)
        self.bullet_speed = 10
        self.bullet_allow_number = 3
        # 关于外星飞船
        self.alien_x_speed = 10
        self.alien_y_speed = 10
        self.alien_score = 50
        # 保存初始的x，y轴的速度,方便在reset游戏的时候重新给定飞船的速度
        self.alien_origin_x_speed = self.alien_x_speed
        self.alien_origin_y_speed = self.alien_y_speed
        self.alien_allow_number = 40
        # 关于游戏模式
        self.game_mode = 2
        # 关于按钮样式
        self.button_style_one = {
            'width': 100,
            'height': 50,
            'bg_color': (20, 20, 20),
            'bg_word': 'play',
            'font_size': 48,
            'font_color': (200, 200, 200),
            'x_pos': int(self.screen_width/2),
            'y_pos': int(self.screen_high/2)
        }
        # 关于游戏动态参数节奏
        self.alien_x_speed_factor = 1.5
        self.alien_y_speed_factor = 1.5
        # 关于记分板
        self.init_score = 0
        self.text_color = (150, 150, 150)
        self.board_right_offset = 20
        self.board_top_offset = 20
        self.board_font_size = 30

    def dynamic_speed(self):
        """动态的增加飞船的速度"""
        self.alien_x_speed *= self.alien_x_speed_factor
        self.alien_y_speed *= self.alien_y_speed_factor

    def reset_speed(self):
        """重新初始化飞船的速度"""
        self.alien_x_speed = self.alien_origin_x_speed
        self.alien_y_speed = self.alien_origin_y_speed




