class Student:
    # __init__ method is used to initialize a values
    # self is a pointer it points the values
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def show_details(self):
        return f'Student: {self.name}, Grade: {self.grade}'

student1 = Student("Arun","A")
student2 = Student("Rahul","B")
print(student1.show_details())
print(student2.show_details())

