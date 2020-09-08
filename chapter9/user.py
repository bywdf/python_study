class User():
    ''''''

    def __init__(self, first_name, lastname):
        ''''''
        self.first_name = first_name
        self.last_name = lastname
        self.login_attempts = 0

    def describe_user(self):
        ''''''
        print("您的名字是" + self.first_name + self.last_name)
    
    def greet_user(self):
        ''''''
        print("你好" + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


zhangsan = User("张", "三")
# zhangsan.describe_user()
# zhangsan.greet_user()
# print(zhangsan.last_name)

# zhangsan.increment_login_attempts()
# zhangsan.increment_login_attempts()
# zhangsan.increment_login_attempts()
# zhangsan.increment_login_attempts()
# print(zhangsan.login_attempts)
# zhangsan.reset_login_attempts()
# print(zhangsan.login_attempts)


class Admin(User):
    def __init__(self, first_name, lastname):
        super().__init__(first_name, lastname)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for i in self.privileges:
            print(self.first_name + i)


# privileges_1 = Admin("lisi", "wu")
# privileges_1.show_privileges()   