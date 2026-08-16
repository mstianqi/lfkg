class Student:
    def __init__(self, name, chinese, math):
        self.name = name
        self.chinese = chinese
        self.math = math

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math}"

    def update_score(self, chinese=None, math=None):
        if self.chinese is not None:
            self.chinese = chinese
        if self.math is not None:
            self.math = math

class EduManagement:
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input("请输入姓名：")
        for s in self.student_list:
            if s.name == name:
                print("已存在，重新输入")
                return
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        if 0<=chinese<=100 and 0<=math<=100:
            stu = Student(name, chinese, math)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("成绩需要在0-100之间")

    def update_student(self):
        name = input("请输入姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                if 0 <= chinese <= 100 and 0 <= math <= 100:
                    s.update_score(chinese,math)
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("成绩需要在0-100之间")
                    return
        print("该学生不存在")

    def delete_student(self):
        name = input("请输入姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("该学生不存在")

    def query_student(self):
        name = input("请输入姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("该学生不存在")

    def list_student(self):
        for s in self.student_list:
            print(s)

    def run(self):
        print(EduManagement.system_name)
        while True:
            print("1.添加 2.修改 3.删除 4.查询 5.查询所有 6.退出")
            choice = input("请输入操作：")

            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        break
                    case _:
                        print("输入错误，请重新输入")
            except Exception as e:
                print("程序出错：", e)

if __name__ == '__main__':
    edu = EduManagement()
    edu.run()