class RecordScore:
    def __init__(self, ai_settings):
        """初始化文件读写类"""
        self.setting = ai_settings
        # 文件路径
        self.file_path = ai_settings.file_path
        self.file_name = ai_settings.file_name
        self.path = self.file_path + self.file_name

    def read_text(self):
        """从制定路径中读取数据，返回一个字符串"""
        with open(self.path) as file_object :
            content = file_object.read()
        return int(content)

    def write_text(self, content):
        """将content写入文件中"""
        with open(self.path, 'w') as file_object:
            file_object.write(content)


