# # 字符串的切片和列表一样
# s = "hello world"
# print(type(s))
# print(s[5])
# print(s[0:2])
# print(s[-7:-12:-1])

# 常用方法
s = "  HELLO-python--"
e1 = s.find("HELLO")
print(e1)
e2 = s.count("O")
print(e2)
su = s.upper()
print(su)
sl = s.lower()
print(sl)
sp = s.split("-")
print(sp)
ss1 = s.strip(" ")
print(ss1)
ss2 = s.strip("-")
print(ss2)
sr = s.replace("-","_")
print(sr)
print(s.startswith("HELLO"))
print(s.endswith("-"))