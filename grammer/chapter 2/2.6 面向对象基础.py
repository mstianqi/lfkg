# class Car:
#     def __init__(self, c_color, c_brand, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#         print("Car对象创建完毕")
#
#     def running(self):
#         print(f"{self.brand}正在行驶中...")
#
#     def total_cost(self, discount, rate):
#         total_cost = self.price * discount + self.price * rate
#         return total_cost
#
# c = Car("red", "BYD", 10000)
# print(c.__dict__)
# c.running()
# total = c.total_cost(0.8, 0.1)
# print(f"总价格：{total}")

# # 魔法方法
# class Car:
#     def __init__(self, c_color, c_brand, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#
#     def __str__(self):
#         return f'{self.color}+{self.brand}+{self.price}'
#     def __eq__(self, other):
#         return self.color == other.color and self.brand == other.brand and self.price == other.price
#     def __lt__(self, other):
#         return self.price < other.price
#
# c1 = Car("red", "BYD", 10000)
# c2 = Car("red", "BYD", 10001)
# print(c1)
# print(c1 == c2)
# print(c1 < c2)

# 实例属性与类属性
class Car:
    wheel = 4  # 类属性
    def __init__(self, c_color, c_brand, c_price):
        self.color = c_color
        self.brand = c_brand
        self.price = c_price
        self.wheel = 2  # 实例属性

c1 = Car("red", "BYD", 10000)
print(c1.wheel)