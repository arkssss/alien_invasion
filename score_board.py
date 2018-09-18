import pygame


class ScoreBoard:
    def __init__(self, screen, ai_setting, init_mode, caption=""):
        self.setting = ai_setting
        # 初始化模式 1为中间的 ， 2为右边的 , 3为右边下面的（显示等级）
        self.init_mode = init_mode
        # 关于屏幕
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 初始化得分板
        self.point = ai_setting.init_score
        self.point_str = str(self.point)
        self.caption = caption
        self.bg_color = ai_setting.bg_color
        self.font = pygame.font.SysFont(None, ai_setting.board_font_size)
        self.text_color = ai_setting.text_color
        self.def_board()

    def def_board(self):
        """字体文件转为surface"""
        self.image = self.font.render(self.caption+self.point_str, True, self.text_color, self.bg_color)
        # 定义得分榜位置
        self.rect = self.image.get_rect()
        if self.init_mode == 2:
            # 置于最右边
            self.rect.right = self.screen_rect.right - self.setting.board_right_offset
            self.rect.top = self.setting.board_top_offset
        elif self.init_mode == 1:
            # 置于顶端
            self.rect.centerx = self.screen_rect.centerx
            self.rect.top = self.setting.board_top_offset
        elif self.init_mode == 3:
            self.rect.right = self.screen_rect.right - self.setting.board_right_offset
            self.rect.top = self.setting.board_level_top_offset

    def draw_board(self, number):
        """根据number绘制得分板"""
        self.update_score(number)
        self.screen.blit(self.image, self.rect)

    def update_score(self, number):
        """更新得分板分数"""
        # 对结果进行10的倍数取整
        # self.point = round(number, -1)
        # 对结果进行千整数分割
        self.point = number
        self.point_str = "{:,}".format(self.point)
        self.def_board()



