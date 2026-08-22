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

class BaoMa:
    def __init__(self, version):
        self.version = version

    def run(self):
        print("宝马正在行驶")

class FuelCar(Car, BaoMa):
    def __init__(self, brand, owner, version):
        Car.__init__(self, brand, owner)
        BaoMa.__init__(self, version)


if __name__ == '__main__':
    c1 = FuelCar('奔驰', '小明', 'V1.0')
    print(c1.__dict__)
    c1.run()
    print(FuelCar.mro())  # 查看FuelCar的方法解析顺序