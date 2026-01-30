# Simple ATM Simulator - PIN Verification
correct_pin = "1234"
attempts = 0
initial_balance = 1000
account_blocked = False

# PIN Verification Logic
while attempts < 3:
    user_pin = input("Enter your 4-digit PIN: ")
    
    if user_pin == correct_pin:
        print("Login Successful!")
        break 
    else:
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"Incorrect PIN. You have {remaining} attempts left.")
        else:
            print("Too many incorrect attempts. Your Account is Blocked!")
            account_blocked = True

# Menu starts ONLY if account is not blocked
if not account_blocked:
    print("Welcome to ATM Menu...")

    while True:  # ATM Menu Loop
        print('\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit')
        inp = input('\nSelect Your Option: ')

        if inp == '1':
            print(f'Your balance is: {initial_balance}')
            
        elif inp == '2':
            deposit = int(input('Enter your deposit amount: '))
            initial_balance += deposit
            print(f'Amount Added! Current balance: {initial_balance}')
            
        elif inp == '3':
            withdraw = int(input('Enter your withdrawal amount: '))
            if withdraw <= initial_balance:
                initial_balance -= withdraw
                print(f'₹{withdraw} debited. Remaining balance: {initial_balance}')
            else:
                print('Insufficient balance!')
                
        elif inp == '4':
            print('Thank you for banking with us!')
            break  # Exit the loop
        
        else:
            print('Invalid Option! Please try again.')