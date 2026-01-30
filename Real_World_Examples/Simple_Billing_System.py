items = {'apple': 100, 'banana': 40, 'orange': 70, 'grapes': 200}
grand_total = 0 

print("--- Welcome to Dhanush Stores ---")

while True:
    user_inp = input('\nEnter the item (or type "exit"): ').lower()

    if user_inp == 'exit':
        print(f'\nOriginal Total: {grand_total}')
        
        # --- Discount Logic Start ---
        if grand_total > 500:
            discount = grand_total * 0.10  # 10% calculate pandrom
            grand_total -= discount        # Total-la irundhu minus pandrom
            print(f'Congrats! You got a 10% discount: -{discount}')
        # --- Discount Logic End ---

        print(f'Your Final Bill: {grand_total} units.')
        print('Thank you for shopping!')
        break # Inga dhaan break use aagudhu!
    
    if user_inp in items:
        quantity = int(input(f'Enter quantity for {user_inp}: '))
        cost = items[user_inp] * quantity
        grand_total += cost 
        print(f'Current Total: {grand_total}')
    else:
        print('Sorry, Item not found.')