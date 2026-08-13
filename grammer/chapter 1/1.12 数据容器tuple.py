# t1 = (1, 2, 3, 4, 5, 6)
# print(type(t1))
# print(t1[0:3:1])
# print(t1.count(3))
# print(t1.index(3))
# a,*b,c = t1
# print(a,b,c)

# # 使用元组交换两个数的值
# a=10
# b=20
# a,b = b,a
# print(a,b)

print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
students = (
    ("001", "小明", 80, 70, 60),
    ("002", "小红", 70, 60, 80),
    ("003", "小强", 60, 50, 40)
)
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{avg:.2f}")
chinese = [s[2] for s in students]
math = [s[3] for s in students]
english = [s[4] for s in students]
print(f"语文最高分：{max(chinese)}，最低分：{min(chinese)}，平均分：{sum(chinese)/len(chinese)}")
print(f"数学最高分：{max(math)}，最低分：{min(math)}，平均分：{sum(math)/len(math)}")
print(f"英语最高分：{max(english)}，最低分：{min(english)}，平均分：{sum(english)/len(english)}")