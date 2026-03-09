""" Aribitary Keyword Arguments - **kwargs """
# ->If you don't know how many keyword arguments are passed in your function on that time use **kwargs
# ->In this way the function will receive a dictionary of arguments and access it accordingly
# ->**kwargs allows a function to accept any number of keyword arguments

# Example

def mobile_brand(**brand):
    print('The Mobile Brand is ' + brand['Model'] + ' and ' + brand['processor'] + ' Processor')
mobile_brand(Model='vivo y20t',processor='Snapdragon',RAM='6GB')

# 1.Using **kwargs with regular arguments:
#  ->you can combine regular arguments with **args
#  ->Regular arguments must come before **args

def My_details(username,**details):
    print('Username:',username)
    for key,value in details.items():
        print(''+ key+':',value)
My_details("dhanush123", age = 21, city = 'kpm', hobby = 'coding')

# 2.You can use both *args and **kwargs in same function
# The Order Must be:
#    -> Regular Parameters
#    -> * args
#    -> **kwargs

# Example - 'Multi-Category Product Adder'

def add_product(product_name,*accessories,**specifications):
    print('Product name:',product_name)
    print('\nAccessories are:')
    for item in accessories:
        print(f'*',item)
    print('\nSpecifications are:')
    for key,value in specifications.items():
        print( key+':',value)
add_product('Gaming Laptop','Wireless Mouse','Cooling Pad','Headset',RAM='16GB', Processor='i7', Storage='512GB', GPU='RTX 3050')

""" Unpacking arguments """
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments

# 3.Unpacking List with *
#  -> If you have values stored in a list, you can use * to unpack them into individual arguments
def show_marks(tamil, english, maths):
    print('Tamil:',tamil,'English:',english,'Maths:',maths)
numbers = [80, 70, 80]
show_marks(*numbers)

# Example for Understanding:

my_list = [1, 2, 3]

# Case 1: print as list
print(my_list)   # Output: [1, 2, 3] (With brackets)

# Case 2: Unpack and print
print(*my_list)  # Output: 1 2 3 (No brackets, separate values)

# 4.Unpacking Dictionary with **
#  -> If you have values stored in a Dictionary, you can use ** to unpack them
def user_profile(name,role,experience):
    print('\n The username is:',name,'\n Role is:',role,'\n Experience is:',experience)
my_data = {
    'name': 'Dhanush',
    'role': 'Python Developer',
    'experience': 'Fresher'
}
user_profile(**my_data)

