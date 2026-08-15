class Student:
    def __init__(self, name, chinese, math):
        self.name = name
        self.chinese = chinese
        self.math = math

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math}"

class EduManagement:
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        name = input("请输入姓名：")
        for s in self.student_list:
            if s.name == name:
                print("已存在，重新输入")
                return
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        if 0<=chinese<=100 and 0<=math<=100:
            stu = Student(name,chinese,math)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("成绩需要在0-100之间")