class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)


class Developer(Employee):
    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language

    def display_details(self):
        super().display_details()
        print("Programming language:", self.language)


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print("Team size:", self.team_size)


developer = Developer("Hassan", "D101", "Python")
manager = Manager("Ayesha", "M201", 8)

developer.display_details()
print()
manager.display_details()
