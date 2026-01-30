# items = {'apple': 100,'banana': 40,'orange': 70,'grapes': 200}
# while True:
#  user_inp = input('Enter the item you want to buy: ')
#  total_cost = 0

#  if user_inp in items:
#     quantity = int(input('Enter the quantity: '))
#     total_cost = items[user_inp] * quantity
#     print(f'The total cost for {quantity} {user_inp}(s) is: {total_cost} units.')
#  else:
#     if user_inp.lower() == 'exit':
#         print('Exiting the billing system. Thank you!')
#         break
#     print('Sorry Item not found.')

items = {'apple': 100, 'banana': 40, 'orange': 70, 'grapes': 60}

# Total bill-a loop-ku veliya vai, appo dhaan adhu reset aagadhu
grand_total = 0 

print("--- Welcome to Dhanush Stores ---")
print(items)

while True:
    user_inp = input('\nEnter the item (or type "exit"): ').lower()

    if user_inp == 'exit':
        print(f'\nYour Grand Total Bill is: {grand_total} units.')
        print('Thank you for shopping!')
        break
    
    if user_inp in items:
        quantity = int(input(f'Enter quantity for {user_inp}: '))
        cost = items[user_inp] * quantity
        
        # Accumulate the cost (Adding to the previous total)
        grand_total += cost 
        
        print(f'Added: {quantity} {user_inp} - Cost: {cost}')
        print(f'Current Total: {grand_total}')
    else:
        print('Sorry, Item not found.')