""" Python Scope """
# A Variable is only available from inside the Region it is created.It is called Scope
# Python follows LEGB rule:
#   -> L for Local Scope
#   -> E for Enclosed Scope
#   -> G for Global Scope
#   -> B for Built in Scope

""" Local Scope """
# A Variable Created inside a function belongs to the local scope of that function and only it is accessed inside the function

# Example:
def local_scope():
    x = 5
    print(x)
local_scope()

""" Enclosing Scope """
# It is often called as Nested Function. If you have one function inside another function the another function can access the main function
# nonlocal keyword:
#   -> when you have to change the outer variable function to inner variable function use nonlocal keyword to change the variable value.
#   -> If you change it normaly in inner variable of outer function variable it don't show error it - Python will understand The user has to create a new variable and it will be access only in Local Scope

# Example:
def greeting_system(name):
    message = 'Welcome to Python World'
    def display_message():
        nonlocal message
        message = 'Welcome to code world'
        print(f'Hello',name,message)
    display_message()
    print(message)
greeting_system('Dhanush')

""" Global Scope """
# If you need to use your variable anywhere in function use variable in outside
# If your variable is inside the function but you have to use in outside use global keyword before variable name

# Example:
x=25
def fav_num():
    print(x)
fav_num()

def total_marks():
    global marks
    marks = 385
total_marks()
print(marks)

""" Built in Scopt """
# In Python have the Default Built in Scopes:
#  -> Functions: print(), len(), sum(), max(), min(), type(), range().
#  -> Constants: None, True, False.
#  -> Exceptions: ValueError, TypeError.

# Example:
# We did not define 'sum' or 'len', but they work automatically.
# This is because they exist in the Built-in Scope.
# If you name your own variable sum, Python will use your variable and ignore the built-in one (which usually causes an error)

numbers = [10, 20, 30, 40, 50]

# 1. Accessing the built-in len() function to get list size
total_elements = len(numbers)

# 2. Accessing the built-in sum() function to add all elements
total_sum = sum(numbers)

# 3. Accessing the built-in print() function to display results
print(f"Total number of items: {total_elements}")
print(f"The sum of all items: {total_sum}")

# --- Pro Tip: How to see everything in Built-in Scope ---
import builtins

# This will list every single name (functions, constants, errors) 
# that Python provides by default without any imports.
print(dir(builtins))