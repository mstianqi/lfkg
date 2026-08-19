# # 读文件
# with open("resources/静夜思.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)
#     f.close()

# 写文件
with open("resources/静夜思.txt", "w", encoding="utf-8") as f:
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
    f.close()