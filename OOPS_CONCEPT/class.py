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
student3 = Student("Babu",'A')
print(student1.show_details())
print(student2.show_details())
print(student3.show_details())

# create class for fruits
class Fruits:
    def __init__(self,fruit_name,fruit_price):
        self.name = fruit_name
        self.price = fruit_price
    def fruits_details(self):
        return f"Fruit name: {self.name} and Price is: {self.price}"
    
fruit1 = Fruits("Apple",40)
fruit2 = Fruits("Orange",60)
print(fruit1.fruits_details())
print(fruit2.fruits_details())




