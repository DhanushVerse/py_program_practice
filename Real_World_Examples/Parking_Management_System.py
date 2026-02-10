total, vehicles = 10, []

while True:
    print(f"\n{'='*10} DHANUSH PARKING {'='*10}\n1. Entry | 2. Exit | 3. Status | 4. Close") 
    choice = input('Select (1-4): ')

    if choice == '1':
        if len(vehicles) < total:  # 0 < 10
            v_no = input('Vehicle No: ')
            vehicles.append(v_no)
            print(f'Parked! Available: {total - len(vehicles)}') # 10 - 1 = 9
        else:
            print('Lot Full!')

    elif choice == '2':
        v_no = input('Vehicle No: ')
        if v_no in vehicles:
            if input('Pay Rs.50: ') == '50':
                vehicles.remove(v_no)
                print('Exit Cleared!')
            else:
                print('Payment Failed!')
        else:
            print('Not Found!')

    elif choice == '3':
        print(f'Total: {total} | Occupied: {len(vehicles)} | Free: {total - len(vehicles)}')

    elif choice == '4':
        print('Shutting down...'); break

    else:
        print('Invalid Option!')