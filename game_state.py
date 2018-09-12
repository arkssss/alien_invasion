import sys


class GameState:
    # 这个类用于保存游戏运行时的参数变化
    def __init__(self, ai_settings):
        self.setting = ai_settings
        self.reset()

    def reset(self):
        self.left_ship = self.setting.limit_ship

    def check_state(self):
        """查看游戏运行时的相关参数，并做相应的应为"""
        if self.left_ship <= 0:
            sys.exit()


