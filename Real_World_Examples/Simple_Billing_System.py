fruits_items = {'apple': 100, 'banana': 40, 'orange': 70, 'grapes': 200, 'guava': 60}
Stock_items = {'apple': 30, 'banana': 60, 'orange': 30, 'grapes': 20, 'guava': 30}
grand_total = 0 

print("--- Welcome to Dhanush fruits shop ---")

while True:
    # Get user input and convert to lowercase for consistency
    user_inp = input('\nEnter the item (or type "exit"): ').lower()

    # Check if the user wants to finish shopping
    if user_inp == 'exit':
        print(f'\nOriginal Total: {grand_total}')
        
        # --- Discount Logic Start ---
        # Apply 10% discount if the total amount exceeds 500
        if grand_total > 500:
            discount = grand_total * 0.10  # Calculate 10% of the total    600 * 0.10 = 60
            grand_total -= discount        # Subtract discount from the grand total 
            print(f'Congrats! You got a 10% discount: -{discount}')
        # --- Discount Logic End ---

        print(f'Your Final Bill: {grand_total} units.')
        print('Thank you for shopping!')
        break # Exit the loop and stop the program
    
    # Check if the entered item exists in our fruits dictionary
    if user_inp in fruits_items:
        # Ask for quantity and calculate the cost for that item
        quantity = int(input(f'Enter quantity for {user_inp}: '))
        if quantity > Stock_items[user_inp]:
            print(f'Sorry, we only have {Stock_items[user_inp]} {user_inp}(s) in stock.')
            continue
        cost = fruits_items[user_inp] * quantity
        grand_total += cost     # Add the item cost to the grand total grand_total = grand_total + cost
        Stock_items[user_inp] -= quantity  # Update stock after purchase //  Stock_items[user_inp] = Stock_items[user_inp] - quantity
        print(f'Current Total: {grand_total}')
        print(f'Stock left for {user_inp}: {Stock_items[user_inp]}')
    else:
        # Show error message if the item is not in the list
        print('Sorry, Item not found.')