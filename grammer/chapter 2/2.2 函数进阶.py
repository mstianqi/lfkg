# # 默认参数
# def reg_stu(name, age, gender, city="北京"):
#     print(f"姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
# stu = reg_stu("小明", 20, "男")
# print(stu)

# # 不定长参数。位置参数和关键字参数的形式不同
# def calc_data(*args, **kwargs):
#     min_data = min(args)
#     max_data = max(args)
#     arg_data = sum(args) / len(args)
#     if kwargs.get("round") is not None:
#         arg_data = round(arg_data, kwargs.get("round"))
#     if kwargs.get("print"):
#         print(f"最大值：{max_data}，最小值：{min_data}，平均值：{arg_data}")
#     return min_data, max_data, arg_data
# print(calc_data(1,2,3,4,5,round=1,print=True))
# print(calc_data(1,2,3))

# # 函数作为参数
# def add (x,y):
#     return x + y
# def calc (a,b,oper):
#     return oper(a,b)
# print(calc(1,2,add))

# 匿名函数。根据每一个元素的字符个数排序
data_list = ["abc", "ab", "abcd", "a"]
data_list.sort(key = lambda x: len(x), reverse = True)
print(data_list)