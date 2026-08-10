# 通过type()获取字面量或变量类型
print(type("hello"))
print(type(10))
print(type(3.14))
print(type(False))
print(type(None))

num = 100
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,str))