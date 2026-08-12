# 计算器
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
oper = input("请输入运算符：")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("输入错误")