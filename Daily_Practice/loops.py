""" while loop
* It is a looping statements which repeadetly performs a set of instructions until the conditions becomes false

# Rules of while loop we should follow in your code:
  * Initialize a looping variable
  * using this looping variable in condition
  * updation of looping variable inside statement block
"""

# program for print python 5 times using while loop

def count():
  count = 1
  while count <= 5:
    print('Python')
    count += 1
# count()

# write a multiplication table for 2

def multiplication_table():
  num = int(input('Enter a number to print multiplication table: '))
  i = 1
  while i <= 10:
   print(i ,'x',num,'=', i * num)
   i += 1

# multiplication_table()

# program for displaying even_odd numbers between 1 to n

def even_odd():
  print('Enter the number between 1 to n:')
  num = int(input())
  i = 1                  
  while i <= num:
    if i % 2 == 0:
      print(i,'is even')
    else:
      print(i,'is odd')
    i+=1

even_odd() 
