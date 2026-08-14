dict1 = {"小明":100, 1:"小红", 3.14:250, (1,2):300}
print(dict1)
dict1["小强"] = 66
dict1["小强"] = 166
print(dict1)
print(dict1["小强"])
print(dict1.get("小强"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
score = dict1.pop("小强")
print(dict1)
del dict1[(1,2)]
print(dict1)
for k,v in dict1.items():
    print(f"{k}：{v}")