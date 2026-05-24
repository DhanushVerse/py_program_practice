""" List """
# List is a collection of items used to store a multiple values at a single variable.
# And list is Ordered,Changable and Allow duplicates.

# Example:
fav_fruits = ['apple','banana','orange']
print(fav_fruits)    # o/p : ['apple','banana','orange']

# List length:
#  -> if you need to find the length of the list use len() function.
fav_fruits = ['apple','banana','orange']
print(len(fav_fruits))   # o/p : 3

# List items - Data types:
#  -> list items can be of any data type
colors = ['red','yellow','green']
numbers = [1,2,3]
boolean = [True,False]

""" Access list: """
# if you need specific element inside list use index value to access it.
# and if the element is at in the end use negative index value [-1]
colors = ['red','yellow','green']
print(colors[0])     # o/p : red
print(colors[-1])    # o/p : green

# Range of indexes:
#  -> you can specify a range of indexes by specifying where to start and where to end the range.
#  -> The search will start at index 2 (included) and end at index 5 (not included).
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])   # o/p : ['cherry','orange','kiwi']

# By leaving out the start value, the range will start at the first item
# By leaving out the end value, the range will go onto the end of the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[:4])   # o/p : ['apple','banana','cherry','orange']
print(fruits[3:])   # o/p : ['orange','kiwi','melon','mango']

# Range of Negative Indexes:
#  -> Specify negative indexes if you want to start the search from the end of the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[-3:-1])  # o/p : ['kiwi','melon']

""" Check if item Exists """
# To determine if a specified item is present in a list use the "in" keyword.
fruits = ['banana','apple','cherry']
if "cherry" in fruits:
    print("Yes, 'cherry' is in the fruits list")  # o/p : Yes, 'cherry' is in the fruits list




