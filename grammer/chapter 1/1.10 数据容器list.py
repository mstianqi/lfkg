# s = [1, 2, 3, "a", "b", True]
# print(type(s))
# print(s[0])
# print(s[-6])
# s[3] = "abc"
# print(s)
# del s[4]
# print(s)

# # 列表list切片
# s = ["a", "b", "c", "d", "e", "f", "g", "h"]
# print(s[0:5:])
# print(s[0:5:2])
# print(s[0:-3:2])

# # 列表的方法
# s = [64, 20, 67, 94, 21, 5, 34, 71, 21]
# s.append(85)
# s.insert(5, 80)
# s.remove(21)
# e = s.pop(5)
# print(e)
# e = s.pop()
# print(e)
# print(s)
# s.sort()
# print(s)
# s.reverse()
# print(s)

# # 合并列表，并去除重复元素
# list1 = [1,2,3,4,4]
# list2 = [4,5,6,7,7]
# list3 = list1 + list2
# # list3 = [*list1, *list2]  # 解包
# list4 = []
# for num in list3:
#     if num not in list4:  # 判断元素是否在列表中
#         list4.append(num)
# print("去除重复元素并排序：", list4)

# # 使用列表推导式计算1-20的平方 要插入列表的数据 for i in 列表
# new_list = [i**2 for i in range(1,21)]
# print(new_list)

# 计算列表中的偶数的平方并组成新列表
num_list = [2,3,4,5,6,7,8]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)