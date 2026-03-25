""" Access the List with for loop """
numbers = [12,5,8,19,22,3,45,10,7,30]
new_list = []
for x in numbers:
    if x > 10 and x % 2 == 0:
        new_list.append(x)
print(new_list)

""" Using List Comprehension """
# Syntax : new_list = [expression for item in iterable if condition]
# Task name : The Number Cruncher
numbers = [12,5,8,19,22,3,45,10,7,30]
new_list = [x for x in numbers if x > 10 and x%2==0]
print(new_list)

""" Why we use List Comprehension """
# Concise - You can replace 4-5 lines of standard code with just a single line.
# Performance - It works slightly faster than general loops in the Python backend.
# Clean - It makes your code look very neat,organized,and professional.

""" How to use if-else in List Comprehension """
# Syntax : [value_if_true if condition else value_if_false for item in iterable]
# Task name : The Odd-Even Labeler
numbers = [1, 4, 7, 10, 13]
labeler = ['Even' if x%2==0 else 'Odd' for x in numbers]
print(labeler)





