class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = 0
        self.__grade = "F"
        self.set_marks(marks)

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
            if marks >= 80:
                self.__grade = "A"
            elif marks >= 60:
                self.__grade = "B"
            elif marks >= 40:
                self.__grade = "C"
            else:
                self.__grade = "F"
            print("Marks updated.")
        else:
            print("Marks must be between 0 and 100.")

    def get_marks(self):
        return self._marks

    def get_grade(self):
        return self.__grade


student1 = Student("Ali", 85)
student2 = Student("Sara", 55)

print(student1.name, "-", student1.get_marks(), "- Grade:", student1.get_grade())
print(student2.name, "-", student2.get_marks(), "- Grade:", student2.get_grade())
student1.set_marks(92)
student2.set_marks(120)
print("Ali's new grade:", student1.get_grade())

try:
    print(student1.__grade)
except AttributeError:
    print("__grade cannot be accessed directly because it is private.")
