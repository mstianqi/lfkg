# # if条件判断
# score = 700
# if score > 680:
#     print("欢迎来到清华！")
# print("welcome!")

# 模拟登录
ok_account = "1888888"
of_password = "666888"
account = input("请输入账号：")
password = input("请输入账号：")
if account == ok_account and password == of_password:
    print("登录成功！")
if account != ok_account or password != of_password:
    print("登录失败！")
    print("账号或密码错误！")