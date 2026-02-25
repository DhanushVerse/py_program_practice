# # get() function is used to get a value in Dictionary
# student = {'name': 'Dhanush','Age': 21, 'Dept': 'BE.CSE'}
# print(student.get('name'))

# # Adding a New Value
# student['Passed out'] = 2025
# print(student)

# # Change Data
# student['Age'] = 22
# print(student)

# # Remove data
# # 1.Using pop
# # 2.Using del keyword

# # pop
# student.pop('Dept')
# print(student)

# # del               
# # using del keyword use Square Brackets[]
# del student['Age']  
# print(student)
# print(len(student))

# books = ['Mastery','Deep Work','Atomic Habits']
# issued_books = {}
# user_id = input('Enter user id:')
# book_name = input('Enter the book name:')
# books.remove(book_name)
# issued_books[user_id] = book_name
# print('Remaining books are:',books)
# print(issued_books)

# print(issued_books.pop(user_id))

Students = {'name': 'Dhanush','name': 'Siva', 'name': 'Babu','Age': [21,21,22]}  
print(Students.get('name')) # If you give Duplicate keys it will store the last one
print(Students.get('Age')) # If you store Multiple Values in One Key use List or Tuple
print(Students.get('Coures','Course not found'))

