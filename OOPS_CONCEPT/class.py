class Student:
    # when object is created __init__ method will be automatically called.
    # self is object reference of the object values
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

print('='*10)
# Create class for fruits:
class Fruits:
    def __init__(self,fruit_name,fruit_price):
        self.name = fruit_name
        self.price = fruit_price
    def fruits_details(self):
        return f"Fruit name: {self.name} and Price is: {self.price}"
    
fruit1 = Fruits("Apple",40)
fruit2 = Fruits("Orange",60)
fruit3 = Fruits("Pomegranates",40)
print(fruit1.fruits_details())
print(fruit2.fruits_details())
print(fruit3.fruits_details())

print('='*10)
# Creating class for Car:
class Car:
    def __init__(self,company,price):
        self.company = company
        self.price = price
    def company_details(self):
        return f"Company name: {self.company} Price: {self.price}"
    
car1 = Car("Rollroce",400000)
car2 = Car("Benz",300000)
car3 = Car("Audi",350000)
print(car1.company_details())
print(car2.company_details())
print(car3.company_details())





