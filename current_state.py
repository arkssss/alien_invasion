# 游戏运行时状态类
class CurrentState:
    def __init__(self, settings):
        # 游戏是否处于激活状态
        self.game_start = False
        self.settings = settings
        # 关于飞船
        self.ship_left_number = settings.ship_allow_number
        # 关于外星舰队
        # self.alien_speed_x = settings.alien_x_speed
        # self.alien_speed_y = settings.alien_y_speed
        # self.alien_x_speed_factor = settings.alien_x_speed_factor
        # self.alien_y_speed_factor = settings.alien_y_speed_factor
        # 关于分数
        self.current_point = settings.init_score
        self.alien_point = settings.alien_score

    def reset_state(self):
        """重置运行状态类"""
        self.current_point = self.settings.init_score
        self.game_start = False
        self.ship_left_number = self.settings.ship_allow_number



