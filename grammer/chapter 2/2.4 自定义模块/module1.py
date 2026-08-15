# __all__ 控制from module1 import * 中导入的功能
__all__ = ['log_separator1', 'log_separator2']

NAME = "小明"

def log_separator1():
    print("-" * 10)

def log_separator2():
    print("6" * 10)

if __name__ == '__main__':
    log_separator1()