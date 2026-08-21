import re

s1 = "18812341234手机号，16612341234手机号"
s2 = "手机号18812341234，手机号16612341234，1881234567890"

result= re.match(r"1[3-9]\d{9}",s1)
print(result.group())
print(result.span())
print(result.start())
print(result.end())

result= re.search(r"1[3-9]\d{9}",s2)
print(result.group())

result= re.findall(r"1[3-9]\d{9}",s2)
print(result)