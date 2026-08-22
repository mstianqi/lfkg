class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name}正在游泳")

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name}正在游泳")

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name}正在游泳")

def go_swimming(duck: Duck):  # 类型注解并不强制，狗和猪也可以调用该方法
    duck.swimming()

if __name__ == '__main__':
    go_swimming(Dog('狗','3'))
    go_swimming(Duck('鸭子','2'))
    go_swimming(Pig('猪','1'))