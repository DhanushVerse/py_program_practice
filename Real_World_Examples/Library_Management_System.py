books_available = ['Mastery', '48 Laws of Power', 'Deep Work', 'Atomic Habits', 'Ikigai']
issued_books = {}  # Format: {UserID: [book1, book2, ...]}

print('\n' + '='*10 + ' SMART LIBRARY SYSTEM ' + '='*10)

while True:
    print('\n1. Search book\n2. Issue Book\n3. Return Book\n4. Check Eligibility\n5. Exit')
    choice = input('Select your Option: ')

    if choice == '1':
        search_book = input('Enter the Book to Search:')
        if search_book in books_available:
            print('Yes it is available')
        else:
            print('No Someone already took it')  

    elif choice == '2':
        user = input('Enter your UserId: ')
        
        # Logic: Check if user already has 3 books
        current_books = issued_books.get(user, [])
        if len(current_books) >= 3:
            print(f'❌ Sorry {user}, you already have 3 books. Return one to take another.')
            continue

        book = input('Enter the book name: ')
        if book in books_available:
            books_available.remove(book)
            
            # User entry illana pudusa create pannum, illana list-la add pannum
            if user in issued_books:
                issued_books[user].append(book)
            else:
                issued_books[user] = [book]
                
            print(f'✅ {user} has successfully issued {book}.')
        else:
            print('⚠️ The Book is not available.')

    elif choice == '3':
        user = input('Enter Your UserID: ')
        if user in issued_books and len(issued_books[user]) > 0:
            print(f'Books you have: {issued_books[user]}')
            book_to_return = input('Which book are you returning?: ')
            
            if book_to_return in issued_books[user]:
                issued_books[user].remove(book_to_return)
                books_available.append(book_to_return)
                print(f'✅ Thank you {user}, {book_to_return} returned successfully.')
            else:
                print('⚠️ You don\'t have this specific book.')
        else:
            print(f'❌ Your ID is not found or you have no books.')

    elif choice == '4':
        user = input('Enter Your UserID: ')
        count = len(issued_books.get(user, []))
        
        if count < 3:
            print(f'ℹ️ You have {count} books. You are ELIGIBLE to take {3 - count} more.')
        else:
            print(f'ℹ️ You have {count} books. You are NOT ELIGIBLE to take more.')

    elif choice == '5':
        print('Exiting... Thank you for using our Library! 👋')
        break
    else:
        print('Invalid option. Please try again.')