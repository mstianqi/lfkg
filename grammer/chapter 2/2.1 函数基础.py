# def hello():
#     print("hello")
# hello()

# # 计算圆的面积和周长，返回多个值会自动封装到元组中
# def circle_area_len(r):
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r: 半径
#     :return: 面积，周长
#     """
#     return round(r * r * 3.14, 1), round(2 * r * 3.14, 1)
# help(circle_area_len)
# al = circle_area_len(10)
# print(al)

# # 函数的嵌套调用
# def fun_a():
#     print("a1")
#     fun_b()
#     print("a2")
# def fun_b():
#     print("b1")
#     fun_c()
#     print("b2")
# def fun_c():
#     print("c1")
# fun_a()

# 统计字符串的元音字母数量
def count(s):
    """
    统计字符串的元音字母数量
    :param s: 字符串
    :return: 元音字母数量
    """
    count = 0
    for w in s:
        if w in "AEIOUaeiou":
            count += 1
    return count
print(count("hello PYTHON"))