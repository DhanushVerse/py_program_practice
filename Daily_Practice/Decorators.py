""" Decorators """
# Decorators is a function that Wraps another function to add extra functionality without changing the Original function.
# A Decorator can be called multiple times.Just place the Decorator above the function to Decorate.

# Example:

def stamp(func):
    def wrapper():
        print('='*3 + 'START' + '='*3)
        func()
        print('='*3 + 'END' + '='*3)
    return wrapper

@stamp
def introduce():
    print('Hello, I am Dhanush!')

@stamp
def age():
    print('I am 22 years old!')

@stamp
def team():
    print('I am Development team!')


introduce()
age()
team()

""" Arguments in the Decorated Function """
# Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function.

# Example:

def check_access(password):
    def decorator(func):
        def wrapper():
            if password == "dhanush123":
                return func()
            else:
                print("Wrong Password Access Denied❌.")
        return wrapper
    return decorator

# we want to use decorater here
pswd = input('Enter the password:')
@check_access(pswd)
def open_locker():
    print("Locker opened!✅")

open_locker()

"""*args and **kwargs usages:"""
# Task for Practice:
#   -> Double it

def double_result(func):
    def wrapper(*args,**kwargs):
        print('Before function call...')
        result = func(*args,**kwargs)
        result = result * 2
        print('After function call...')
        return result
    return wrapper

@double_result
def add(a,b):
    return a + b
print(add(5,5))

@double_result
def multiply(a,b,c):
    return a * b * c
print(multiply(2,3,4))

""" Decorators with Parameters """
# A decorator with parameters is just a wrapper around a decorator — so you can pass your own settings into it.

# Example:
# String Length Validator

def validate_length(min,max):
    def decorator(func):
        def wrapper(text):
            if len(text) < min:
                return '❌error'
            elif len(text) > max:
                return '❌error'
            else:
                return func(text)
                pass
        return wrapper
    return decorator

@validate_length(3,10)
def set_username(name):
    return f'Username set: {name}'

user_name = input('Enter the valid Username:')
print(set_username(user_name))


""" Preserving Function Metadata """
# Function in Python has Metadata that can be accessed using the __name__ and __doc__ attributes.

# Example:
def myfunction():
    return 'Hello welcome to Code world'
print(myfunction.__name__)

# note:
#  -> But when a function is decorated the metadata of the original function is lost
#  -> To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring

def changecase(func):
    def wrapper():
        return func().upper
    return wrapper
@changecase
def Mycase():
    return 'welcome to py world'
print(Mycase.__name__)                         # o/p : wrapper
print(Mycase.__doc__)                          # o/p : None


""" Import functools.wraps """
# Example:
import functools
def changecase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper
    return wrapper
@changecase
def myfunction():
    return 'have a great day!'
print(myfunction.__name__)                     # o/p : myfunction



    