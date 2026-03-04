books_available = ['Mastery', 'Deep Work', 'Atomic Habits','Ikigai']
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
        current_books = issued_books.get(user_id,[])
        if len(current_books) >= 3:
            print('❌ Sorry you have already 3 books.Return one to take another')
            continue
        book = input('Enter the book name to issue:')
        if book in books_available:
            books_available.remove(book)
        # create user to store
            if user_id in issued_books:
              issued_books[user_id].append(book)
              print(f'{user_id} has successfully issued {book}✅')
            else:
              issued_books[user_id] = [book]
              print(f'{user_id} has successfully issued {book}✅')
        else:
            print('Book is not available')
    
    elif choice == '3':
        user_id = input('Enter the userid:')
        if user_id in issued_books:
            print('The books you have:',issued_books.get(user_id,[]))
            book = input('Enter the bookname to return:')
            if book in issued_books[user_id]:
                issued_books[user_id].remove(book)
                books_available.append(book)
                print(f'The {user_id} has successfully return the book {book}✅')
            else:
                print(f'{user_id} has no records')
                if not issued_books[user_id]:
                    del issued_books[user_id]
                    print('You Currently have no books I delete your Id for clean space')
                else:
                  print(f'Sorry the book is not available in your id')
    
    elif choice == '4':
        user_id = input('Enter the userid:')
        if user_id in issued_books:
            current_books = issued_books.get(user_id,[])
            count = len(current_books)
            if count < 3:
                total = 3 - count
                print(f'You are eligible to take {total} book left')
            else:
                print(f'You are not ❌ eligible to take books further because you have 3 book')
        else:
            print(f'You are eligible to take books')
    
    elif choice == '5':
        print(f'Thank you for using our Library...👋')
        break
        
        