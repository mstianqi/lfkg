import re

s = "手机号18812341234，测试188，手机号15512341234，QQ号88886666，邮箱python666@qq.com"
s2 = "时间2026-01-01，测试"

print(re.findall(r"188.*",s))
print(re.findall(r"188.?",s))
print(re.findall(r"188.+",s))
print(re.findall(r"188\d{8}",s))
print(re.findall(r"1[56]\d{8}",s))
print(re.findall(r"1(?:5|6)\d{8}",s))
print(re.findall(r"1[^56]\d{8}",s))
print(re.findall(r"\w+@\w+\.\w+",s))
print(re.findall(r"\d{4}-\d{2}-\d{2}",s2))