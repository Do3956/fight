class ConfigError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(f'配置错误：{self.value}')
