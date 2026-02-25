# count = 10
# while count > 0:
#     print(count)
#     count -=1


# While loop password check program

# password = "" 
# attempts = 0
# while attempts < 3:
#     password = input('Enter the Password:')
#     if password == 'Dhanush21':
#         print('Access Granted')
#         break                              # If User entered Correct Password it would break from the loop
#     attempts += 1
#     if attempts == 3:
#         print('Account Blocked')

# Secret Game

secret_number = 5
while True:
    guess = int(input('Guess the number:'))
    if guess == secret_number:
        print('You Won!')
        break
    elif guess < secret_number:
        print('Too Low!')
    elif guess > secret_number:
        print('Too High!')

