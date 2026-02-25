books_available = ['Mastery', 'Deep Work', 'Atomic Habits']
issued_books = {}  # Dictionary to store {user_id: book_name}

while True:
    print('\n1. Search book\n2. Issue book\n3. Return book\n4. Check Eligibility\n5. Exit')
    choice = input('Select an option: ')

    if choice == '1':
        search_book = input('Enter the book name: ')
        if search_book in books_available:
            print(f'Yes, the book "{search_book}" is available.')
        else:
            print(f'Sorry, "{search_book}" is currently not available.')

    elif choice == '2':
        user_id = input('Enter your UserId: ')
        # Check if user already has a book
        if user_id in issued_books:
            print(f'You already have "{issued_books[user_id]}". Return it to take another.')
        else:
            issue_book = input('Enter the book name to issue: ')
            if issue_book in books_available:
                books_available.remove(issue_book)
                issued_books[user_id] = issue_book
                print(f'User {user_id} has successfully issued "{issue_book}" ✅')
            else:
                print('Sorry, that book is not in our library.')

    elif choice == '3':
        user_id = input('Enter your UserId: ')
        if user_id in issued_books:
            returned_book = issued_books.pop(user_id)
            books_available.append(returned_book)
            print(f'{user_id} has successfully returned "{returned_book}" ✅')
        else:
            print(f'No records found for User ID: {user_id}')

    elif choice == '4':
        user_id = input('Enter your UserId: ')
        # Eligibility check: User kitta book illena eligible
        if user_id not in issued_books:
            print('Yes, you are eligible to take a book.')
        else:
            print(f'Not eligible! You already have "{issued_books[user_id]}".')

    elif choice == '5':
        print('Thank you for using our Library! 🙌')
        break
    else:
        print('Invalid option! Try again.')