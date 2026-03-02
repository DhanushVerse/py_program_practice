books = ['Mastery','Deep Work','Atomic Habits','Ikigai']
issued = {}
user = input('Enter your userid:')
book = input('Enter the book you need:')
current_books = issued.get(user,book,[])
print(current_books)


