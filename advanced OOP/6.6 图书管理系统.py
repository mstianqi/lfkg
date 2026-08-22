class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):
        self.__available_num += 1
        return True

    def get_available_num(self):
        return self.__available_num

# 会员父类
class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrowed_books = []

    def borrow_book(self, book):
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，您的借阅数量已达上限")
            return False
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"成功借阅 {book.title}")
            return True
        else:
            print("已被借完")
            return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"归还 {book.title} 成功")
        else:
            print(f"没有借阅 {book.title}")

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    def get_max_books(self) -> int:
        pass

# 普通会员
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

# VIP会员
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level

    def get_max_books(self) -> int:
        return 6 + self.vip_level