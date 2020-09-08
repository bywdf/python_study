class Privileges():
    def __init__(self, privileges):
        self.privileges = []
    def show_privileges(self):
        for i in self.privileges:
            print(i)


class Admin(Privileges):
    def __init__(self, privileges):
        super().__init__(privileges)


susu = Admin("1")
susu.privileges = ["1", "2", "3"]
susu.show_privileges()