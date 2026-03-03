""" Function """
# 1.Function is a block of code which Only runs when it is called
# 2.A Function can return data as a result
# 3.Function can helps us to avoid code repetation

""" Function names rules """
# 1.Function name start with underscore or letters
# 2.A Function can contain letters underscores or numbers
# 3.It is Case Sensitive both uppercase and lowercase letters are different in python

""" Function Return values """
# 1.A function can return the values if you are use to save in a variable and use it later
# 2.Without Return function can return none.
# 3.A function reaches return statement it stops executing and sends the result back

# Example 

def my_code():
    return 'This is my code'
mycode = my_code()
print(mycode)

# # Multi Currency Calculator

def convert_to_usd(ruppees):
    convert_usd = ruppees / 83
    return convert_usd
amount_in_inr = int(input('Enter a amount in INR:'))
result_in_usd = convert_to_usd(amount_in_inr)
print('Your amount in USD is:',result_in_usd)

# # Lucky number generator

def get_lucky_number():
    lucky_num = 5
    return lucky_num
lucky_num_generator = get_lucky_number()
print(lucky_num_generator)

# The Secret Password Checker

def check_password():
    passwrd = input('Enter the password:')
    if passwrd == 'Python123':
        return True
    
    return False
psd_chk = check_password()
print(psd_chk)




