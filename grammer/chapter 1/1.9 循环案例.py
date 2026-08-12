# """
#         案例1：根据输入的用户名密码执行登录操作，具体要求如下：
#         1.正确的用户名和密码为admin/666888
#         2，输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
#         3．输入的用户名和密码不能为空！
#         4，登录成功：输出“登录成功"
#         5，登录失败：输出“用户名或密码错误，请重新输入！”
# """
# while True:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == "" or password == "":
#         print("用户名和密码不能为空！")
#         continue
#
#     if username == "admin" and password == "666888":
#         print("登录成功")
#         break
#     else:
#         print("用户名或密码错误，请重新输入！")

# 猜数字
import random
random_num = random.randint(1,100)
while True:
    num = int(input("猜数字："))
    if num > random_num:
        print("太大了")
    elif num < random_num:
        print("太小了")
    else:
        print("猜对了")
        break