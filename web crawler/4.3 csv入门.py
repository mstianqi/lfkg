import csv

with open("resources/01.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别"])
    writer.writeheader()
    writer.writerow({"姓名": "小明", "年龄": "18", "性别": "男"})
    writer.writerow({"姓名": "小红", "年龄": "17", "性别": "女"})

with open("resources/01.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)