class Car:
    def __init__(self, brand, owner):
        self.brand = brand
        self.__owner = owner  # 私有属性

    def run(self):
        print(f"{self.__owner}的{self.brand}正在行驶")
        self.__control()

    def __control(self):  # 私有方法
        print(f"{self.brand}正在控制油门")

    def get_owner(self):
        return self.__owner

if __name__ == '__main__':
    car = Car("奔驰","小明")
    car.run()
    print(car.get_owner())