import json

# # 写入json
# user = {
#     "name": "小明",
#     "age": 18
# }
# with open("resources/test.json", "w", encoding="utf-8") as f:
#     json.dump(user, f, ensure_ascii=False, indent=4)

# 读取json
with open("resources/test.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
    print(type(data))