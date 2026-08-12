# 通过type()获取字面量或变量类型
print(type("hello"))
print(type(10))
print(type(3.14))
print(type(False))
print(type(None))

# 通过isinstance()判断类型是否匹配
num = 100
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,str))

# 三引号定义字符串，可以定义多行
s1 = """这是第一行
这是第二行
这是第三行"""
print(s1)

# 拼接字符串的三种方式
name = "小明"
age = 18
pro = "计算机科学与技术"
hobby = "python"
message = "大家好，我是" + name + "，我今年" + str(age) + "岁，我的专业是" + pro + "，我的爱好是" + hobby
print(message)
print("大家好，我是%s，我今年%s岁，我的专业是%s，我的爱好是%s"%(name,age,pro,hobby))
print(f"大家好，我是{name}，我今年{age}岁，我的专业是{pro}，我的爱好是{hobby}")