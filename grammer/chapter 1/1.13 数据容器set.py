s1 = {100,200,300,400,500}
print(s1)
s1.add(600)
print(s1)
s1.remove(100)
print(s1)
e = s1.pop()
print(e)
print(s1)
s1.clear()
print(s1)
s2 = {"a","b","c","d"}
s3 = {"a","b","e","f"}
print(s2.difference(s3))  # 差集
print(s2 - s3)
s4 = {s for s in s2 if s not in s3}  # 集合推导式
print(s4)
print(s3.difference(s2))
print(s3 - s2)
print(s2.union(s3))  # 并集
print(s2 | s3)
print(s2.intersection(s3))  #交集
print(s2 & s3)