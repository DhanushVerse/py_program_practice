""" Arbitary arguments """
# 1.When you don't know how many arguments are passed in the function we use *args
# 2.In this *args are stored in tuple collector
# 3.Arbitary arguments are often shortend *args in Python Documentation

def add_items_cart(*items):
    print(f'The items are:',items[2])
add_items_cart('Milk','Bread','Egg')

""" Using args with Regular Parameter """
# 1.You can combine Regular Parameter with *args
# 2.Regular Parameter must come in before *args

def Names(greeting,*names):
    for name in names:
        print(greeting,name)
Names('Hello','Dhanush','Vengat','Siva')

# Examples
# 1.*args is useful when you create a flexible function

def Add(*numbers):
    total = 0
    for num in numbers:
        total += num   # total = total + num
    return total
print(Add(2,3,4))

# Infinite Receipt Generator

def calculate_total(tax_rate,*items):
    total = sum(items)
    subtotal = total * tax_rate
    print(subtotal)
calculate_total(0.10,5,10,15)