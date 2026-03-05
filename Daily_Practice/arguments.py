""" Argument """
# 1.Information can passed into function as Arguments
# 2.Arguments are specified after the function name inside the parenthesis

""" Parameters """
# 1.Parameters are variable listed inside the parenthesis of function definition

# Example:

def my_func(name):    # name is a parameter
    return f'Hello {name}'
myfunc = my_func('Dhanush')  # dhanush is an argument
print(myfunc)

# 1.Number of Arguments:

def my_name(fname,lname):
    return f'Hello {fname} {lname}'
myname = my_name('Dhanush','Aranganathan')
print(myname)

# 2.Default Parameter Values:

def fav_color(color='blue'):
    return f'My favourite color is {color}'
favclr = fav_color()
print(favclr)

# 3.Keyword Argument:
# 1.You can send the arguments with keys = value syntax
# 2.The order of Arguement is does not matter in keyword argument you can change by your way 

def my_details(name,age):
    return f'My name is {name} and my age is {age}'
mydetails = my_details(age=21,name='Dhanush')
print(mydetails)

# 4.Positional Arguments:
# 1.When you call a function with arguments without using keyword,they are called as Positional Arguments
# 2.Order Matters in Positional Arguments

def my_info(name,occupation):
    return f'My name is {name} and Im working in {occupation}'
myinfo = my_info('Dhanush','IT')
print(myinfo)

# 5.Mixing Positional and Keyword Arguments:
# 1.you can mix positional and keyword Arguments in function call
# 2.but positional arguments comes first and then remaining arguments

def my_com_info(age,dept,name):
    return f'Im {name} and my age is {age} and I worked in {dept} team'
mycom_info = my_com_info(21,'Development',name='Dhanush')
print(mycom_info)

# 6.Passing Different Data type as an argument:
# 1.You can any data type as an argument in a function (string,number,list,dictionary)
# 2.The Data can be preserved inside the function

def my_fav_cartoons(cartoons):
    for cartoon in cartoons:
        print(cartoon)

My_fav_cartoons = ['Doreamon','Shincan','Jackie Chan']
my_fav_cartoons(My_fav_cartoons)

# Sending Dictionary as an argument

def My_dts(details):
    print('Name:',details['Name'])
    print('age:',details['age'])

my_details = {'Name': 'Dhanush', 'age': 21}
My_dts(my_details)

# 7.Returning Different Data types
# 1.Function can return any data type (List,tupe,Dictionary and more..)

def my_fruits():
    return ['apple','banana']
fruits = my_fruits()
print(fruits[0])
print(fruits[1])

# return tuple data type

def my_color():
    return ('black','green')
x,y = my_color()
print('clr1:',x)
print('clr2:',y)

# 8.Positional Only Arguments:
# 1.You can specify only the positional arguments use in function
# 2.In this we have to use , / to use only if it is satisfy Positional argument 

def My_name(name,/):
    return f'My name is:{name}'
Name = My_name('Dhanush')
print(Name)

# Note:
#  -> If you use ,/ in positional argument and you pass the argument in keys and value it will show error.

# def my_hobby(hobby,/):
#     return f'My Hobby is {hobby}'
# My_hobby = my_hobby(hobby='Music')
# print(My_hobby)

# 9.Keyword Only Arguments:
# 1.You can specify to use only Keyword arguments in function
# 2.In this we have to use * before the arguments

def fav_sports(*,sport):
    return f'My favourite sport is {sport}'
sports = fav_sports(sport='Kabadi')
print(sports)

# Note:
#  -> If you use * in keyword argument but can you pass Positional arguments it will give you error.

# def year(*,year):
#     return f'year: {year}'
# cu_year = year(2026)

# 10.Combining Positional Only and Keyword Only
# 1.When you want to use Positional use -> ,/ after arguments
# 2.then you want to use Keyword argument use -> * before arguments

def My_function(a,b,/,*,c,d):
    return a+b+c+d
func = My_function(5,3,c=2,d=3)
print(func)