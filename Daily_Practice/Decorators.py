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

introduce()
age()

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