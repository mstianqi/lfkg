# dict1 = {"小明":100, 1:"小红", 3.14:250, (1,2):300}
# print(dict1)
# dict1["小强"] = 66
# dict1["小强"] = 166
# print(dict1)
# print(dict1["小强"])
# print(dict1.get("小强"))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# score = dict1.pop("小强")
# print(dict1)
# del dict1[(1,2)]
# print(dict1)
# for k,v in dict1.items():
#     print(f"{k}：{v}")

# 模拟购物车
menu = "1.添加 2.修改 3.删除 4.查询 5.退出"
shopping_cart = {}
while True:
    print(menu)
    choice = input("请输入操作：")
    match choice:
        case "1":
            name = input("请输入商品名称：")
            if name in shopping_cart:
                print("商品已存在，请重新输入")
            else:
                price = float(input("请输入商品价格："))
                num = input("请输入商品数量：")
                shopping_cart[name] = {"price": price, "num": num}
                print("添加成功")
        case "2":
            name = input("请输入商品名称：")
            if name not in shopping_cart:
                print("商品不存在，请重新输入")
            else:
                price = float(input("请输入商品价格："))
                num = input("请输入商品数量：")
                shopping_cart[name] = {"price": price, "num": num}
                print("修改成功")
        case "3":
            name = input("请输入商品名称：")
            if name in shopping_cart:
                del shopping_cart[name]
                print("删除成功")
            else:
                print("商品不存在，请重新输入")
        case "4":
            name = input("请输入商品名称：")
            if name in shopping_cart.keys():
                info = shopping_cart[name]
                print(f"商品名称：{name}，商品价格：{info["price"]}，商品数量：{info["num"]}")
            else:
                print("商品不存在，请重新输入")
        case "5":
            print("退出")
            break
        case _:
            print("输入错误，请重新输入")