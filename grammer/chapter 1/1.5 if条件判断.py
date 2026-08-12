# # if条件判断
# score = 700
# if score > 680:
#     print("欢迎来到清华！")
# print("welcome!")

# # 模拟登录
# ok_account = "1888888"
# of_password = "666888"
# account = input("请输入账号：")
# password = input("请输入密码：")
# if account == ok_account and password == of_password:
#     print("登录成功！")
# else:
#     print("登录失败！")
#     print("账号或密码错误！")

# # 判断是闰年还是平年
# year = int(input("请输入年份："))
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# 判断三角形类型
a = int(input("请输入第一个边的边长："))
b = int(input("请输入第一个边的边长："))
c = int(input("请输入第一个边的边长："))
if a + b > c and a + c > b and b + c > a:
    if a==b and b==c:
        print(f"{a} {b} {c} 这三个边构成等边三角形")
    elif a==b or b==c or a==c:
        print(f"{a} {b} {c} 这三个边构成等腰三角形")
    else:
        print(f"{a} {b} {c} 这三个边构成普通三角形")
else:
    print(f"{a} {b} {c} 这三个边不构成三角形")