# # 遍历输入的字符串 for 元素 in 待处理数据集
# msg = input("请输入需要遍历的字符串：")
# for s in msg:
#     print(f"元素：{s}")
# print("遍历结束")

# # 1-100的奇数之和
# total = 0
# for i in range(1,100,2):
#     total += i
# print("1-100的奇数之和为：", total)

# # 1-100的3的倍数之和
# total = 0
# for i in range(1,101):
#     if i % 3 == 0:
#         total += i
# print("1-100的3的倍数之和为：", total)

# # 打印长方形
# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))
# for j in range(n):
#     for i in range(m):
#         print("*", end="  ")
#     print()

# 打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()