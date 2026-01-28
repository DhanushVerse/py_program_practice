initial_balance = 1000  # Setting the starting bank balance

while True:  # Starts an infinite loop to keep the program running
    print('\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit')
    inp = input('\nSelect Your Option: ')  # Taking user input for choice

    if inp == '1':
        # Display the current balance stored in the variable
        print(f'Your balance is: {initial_balance}')
        
    elif inp == '2':
        # Taking the deposit amount and converting it to an integer
        deposit = int(input('Enter your deposit amount: '))
        initial_balance += deposit  # Adding the deposit to the current balance
        print(f'Amount Added! Your Current balance is: {initial_balance}')
        
    elif inp == '3':
        # Taking the withdrawal amount and checking if it's possible
        withdraw = int(input('Enter your withdrawal amount: '))
        if withdraw <= initial_balance:
            initial_balance -= withdraw  # Subtracting amount from the balance
            print(f'₹{withdraw} debited from your account')
            print(f'Remaining balance: {initial_balance}')
        else:
            # Message when the user tries to withdraw more than they have
            print('Insufficient balance!')
            
    elif inp == '4':
        # Breaking out of the loop to end the program
        print('Thank you for banking with us!')
        break  
    
    else:
        # Handling any input that is not 1, 2, 3, or 4
        print('Invalid Option! Please try again.')