""" Decorators """
# Decorators is a function that Wraps another function to add extra functionality without changing the Original function

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