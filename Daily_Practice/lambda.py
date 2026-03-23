""" Lambda function """
# A Lambda function is a small anonymous function
# lambda function can take any number of arguments with only one expression

""" Syntax """
# lambda arguments : expression
#   -> The expression is executed and the result is returned.

# Example:
add = lambda a : a + 10
print(add(2))

mul = lambda a,b : a * b
print(mul(2,5))

""" Normal function with Inside Lambda function """
# In this case we use lambda function inside and return a simple logic
# Example:
#  -> Power Multiplier:

def my_power_machine(p):
    return lambda base : base ** p

square_maker = my_power_machine(2)
cube_maker = my_power_machine(3)

sqrt = int(input('Enter the number of square:'))
print(f'The square of {sqrt} is:',square_maker(sqrt))

cbrt = int(input('Enter the number of cube:'))
print(f'The cube of {cbrt} is:',cube_maker(cbrt))


""" Lambda with Built-in Functions """
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map():
#  -> The map() function applies a function to every item in an iterable
numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x *2 , numbers))
print(f'The Doubled numbers are:',doubled)

# Using Lambda with filter():
#  -> The filter() function creates a list of items for which a function returns True
numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f'The Odd numbers are:',odd_numbers)

# Using Lambda with sorted():
#  -> The sorted() function can use a lambda as a key for custom sorting

colors = ['Yellow','Black','Green','Blue','Red']
sorted_words = sorted(colors, key=lambda x: len(x))
print(f'The sorted words are:',sorted_words)





