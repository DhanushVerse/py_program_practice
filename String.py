""" String
* It is basically the sequence of characters
* Any Desired Character can be accessed using the index.
* String Can be Created using double quote or single quotes
"""

# Example

str = 'Hello Good Morning'
print(str[2])
print(str[8])

# Find the length of the string

msg = 'Good bye'
print(len(msg))

# Traverse a string using while loop

Name = 'Dhanush'
index = 0
while index < len(Name):
    result = Name[index]
    print(result)
    index +=1

# Traverse a string using For loop

info = 'Welcome'
for i in range(0,len(info)):
    final = info[i]
    print(final)
    i +=1

# program for display set of strings using range() function

bike_name = ['Splendor','HF-Deluxe','NS-160','UNICORN 160']
print('The bike names are:')
for i in range(len(bike_name)):
    print(bike_name[i],end=' ')
