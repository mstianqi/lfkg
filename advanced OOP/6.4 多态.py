class Car:
    def __init__(self, brand, owner):
        self.brand = brand
        self.__owner = owner  # 私有属性

    def run(self):
        print(f"{self.__owner}的{self.brand}正在行驶")

    def __control(self):  # 私有方法
        print(f"{self.brand}正在控制油门")

    def get_owner(self):
        return self.__owner

    def charge(self):
        print(f"{self.brand}正在补充燃料")

class FuelCar(Car):
    def charge(self):
        # 子类可以继承，也可以调用父类的方法
        print(f"{self.brand}正在加油")

class ElectricCar(Car):
    def charge(self):
        # 子类可以继承，也可以调用父类的方法
        print(f"{self.brand}正在充电")

def handle_charge(car: Car):  # 类型注解
    car.charge()

if __name__ == '__main__':
    c1 = FuelCar("奔驰","小明")
    c2 = ElectricCar("宝马","小红")
    handle_charge(c1)
    handle_charge(c2)