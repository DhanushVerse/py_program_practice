def addition(num1,num2):           # addition function   
    total = num1 + num2
    return f'{num1} + {num2} = {total}'
    
def subtraction(num1,num2):        # subtraction function     
    total = num1 - num2
    return f'{num1} - {num2} = {total}'

def multiplication(num1,num2):     # multiplication function
    total = num1 * num2
    return f'{num1} * {num2} = {total}'

def division(num1,num2):           # division function
    total = num1 / num2
    return f'{num1} / {num2} = {total}'

def modulus(num1,num2):            # modulus function
    total = num1 % num2
    return f'{num1} % {num2} = {total}'

def power(num1,num2):              # power function
    total = num1 ** num2
    return f'{num1} ** {num2} = {total}'

show_history = []


while True:
    print('='*5 + ' CALCULATOR ' + '='*5,'\n')
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulas\n6. Power\n7. Show history\n8. Exit')
    option = input('Choose an option:')

    if option == '7':
        for item in show_history:
            print(item)
        continue

    if option == '8':
        print('Thank you!')
        break
    
    num1 = int(input('Enter number1:'))
    num2 = int(input('Enter number2:'))
    
    if option == '1':
        add = addition(num1,num2)
        print(add)
        show_history.append(add)
    
    elif option == '2':
        sub = subtraction(num1,num2)
        print(sub)
        show_history.append(sub)

    elif option == '3':
        mul = multiplication(num1,num2)
        print(mul)
        show_history.append(mul)

    elif option == '4':
        div = division(num1,num2)
        print(div)
        show_history.append(div)
    
    elif option == '5':
        mod = modulus(num1,num2)
        print(mod)
        show_history.append(mod)
    
    elif option == '6':
        power_result = power(num1,num2)
        print(power_result)
        show_history.append(power_result)

    else:
        print('Invalid option')


