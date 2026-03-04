""" Argument """
# 1.Information can passed into function as Arguments
# 2.Arguments are specified after the function name inside the parenthesis

""" Parameters """
# 1.Parameters are variable listed inside the parenthesis of function definition

# Example

def my_func(name):    # name is a parameter
    return f'Hello {name}'
myfunc = my_func('Dhanush')  # dhanush is an argument
print(myfunc)

# Number of Arguments

def my_name(fname,lname):
    return f'Hello {fname} {lname}'
myname = my_name('Dhanush','Aranganathan')
print(myname)

# Default Parameter Values

def fav_color(color='blue'):
    return f'My favourite color is {color}'
favclr = fav_color()
print(favclr)

# Keyword Argument
# 1.You can send the arguments with keys = value syntax
# 2.The order of Arguement is does not matter in keyword argument you can change by your way 

def my_details(name,age):
    return f'My name is {name} and my age is {age}'
mydetails = my_details(age=21,name='Dhanush')
print(mydetails)

# Positional Arguments
# 1.When you call a function with arguments without using keyword,they are called as Positional Arguments
# 2.Order Matters in Positional Arguments

def my_info(name,occupation):
    return f'My name is {name} and Im working in {occupation}'
myinfo = my_info('Dhanush','IT')
print(myinfo)

# Mixing Positional and Keyword Arguments
# 1.you can mix positional and keyword Arguments in function call

def my_com_info(age,dept,name):
    return f'Im {name} and my age is {age} and I worked in {dept} team'
mycom_info = my_com_info(21,'Development',name='Dhanush')
print(mycom_info)