books_available = ['Mastery','48 Laws of Power','Deep Work','Atomic Habits','Ikigai']
issued_books = {} # keys and values
print('\n' + '='*10 + 'SMART LIBRARY SYSTEM' + '='*10)
while True:
    print('\n1. Search book\n2. Issue book\n3. Return book\n4. Check Eligibility\n5. Exit')
    choice = input('Select your Option:')
    if choice == '1':                              # Search book
        search_book = input('Enter the book name to search:')
        if search_book in books_available:
            print('Yes it is available✅')
        else:
            print('No Someone already took it❌')
    elif choice == '2':                             # Issue book
        user = input('Enter the UserId:')
        # check user has already 3 books
        current_books = issued_books.get(user,[])  # userid - > 'Mastery','Deepwork','Ikigai'
        if len(current_books) >= 3:
            print(f'❌Sorry you have already 3 books.Return one to take another')
            continue # skip
        book = input('Enter the book name:')
        if book in books_available:
            books_available.remove(book)

            if user in issued_books:
                issued_books[user].append(book)
                print(f'{user} has successfully issued {book}✅')
            else:
                issued_books[user] = [book]    # 'abc21': 'mastery'
                print(f'{user} has successfully issued {book}✅')
        else:
            print('The Book is not available.')
    elif choice == '3':                                          # Return book
        user = input('Enter your userId:')
        if user in issued_books:
            print('The books you have:',issued_books.get(user,[]))
            return_book = input('Which book you are Returning now:')
            if return_book in issued_books[user]:
                issued_books[user].remove(return_book)
                books_available.append(return_book)
                print(f'{user} has successfully Returned the book {return_book}✅')
        else:
            print('The Book is not in your records')

    elif choice == '4':                      # Check Eligibility
        user = input('Enter your userId:')
        if user in issued_books:
            count = len(issued_books[user])
            print('The books you have:',issued_books.get(user,[]))
            if count == 3:
                print(f'You are Not Eligible to take book❌')
                continue
            elif count == 2:
                print(f'You are Eligible to take 1 book')
            elif count == 1:
                print(f'You are Eligible to take 2 books')
        else:
            print(f'You have no records')

    elif choice == '5':
        print(f'Thank you for Using Our Library...🙌')
        break

            
            



            

            
        


        




    
    




    






