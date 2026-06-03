def addition(num1,num2):
    total = num1 + num2
    return total

def subtraction(num1,num2):
    total = num1 - num2
    return total

def multiplication(num1,num2):
    total = num1 * num2
    return total

def division(num1,num2):
    total = num1 / num2
    return total

def modulus(num1,num2):
    total = num1 % num2
    return total

def power(num1,num2):
    total = num1 ** num2
    return total


while True:
    print('='*5 + ' CALCULATOR ' + '='*5,'\n')
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulas\n6. Power\n7. Exit')
    option = input('Choose an option:')

    if option == '7':
        print('Thank you!')
        break
    
    num1 = int(input('Enter number1:'))
    num2 = int(input('Enter number2:'))

    if option == '1':
        add = addition(num1,num2)
        print(add)
    elif option == '2':
        sub = subtraction(num1,num2)
        print(sub)
    elif option == '3':
        mul = multiplication(num1,num2)
        print(mul)
    elif option == '4':
        div = division(num1,num2)
        print(div)
    elif option == '5':
        mod = modulus(num1,num2)
        print(mod)
    elif option == '6':
        power_result = power(num1,num2)
        print(power_result)
    else:
        print('Invalid option')


