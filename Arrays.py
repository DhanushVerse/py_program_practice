""" Array is a Data Structure used to store a list of elements 
  Creation of Arrays:
    arr = [1,2,3,4]
"""

def Array_Creation():
    arr = [1,2,3,4]
    print('The elements in array is:')
    for i in range(len(arr)):
        print(arr[i])

Array_Creation()

# Operation in Array

# 1.append is used for add the elements in a end of tha array
# syntax: append(value)

def Adding_element():
    arr = [1,2,3,4]
    print('The elements in array is:')
    for i in range(len(arr)):
        print(arr[i])
    arr.append(5)
    print('Now the current elements are:')
    for i in range(len(arr)):
        print(arr[i])

Adding_element()

# 2.Insert we can insert a value at any desired location.
# syntax: insert(index,value)

def Insert_element():
    arr = [1,2,3,5]
    print('The elements in array are:')
    for i in range(len(arr)):
        print(arr[i])
    arr.insert(3,4)
    print('Now the current elements in array is:')
    for i in range(len(arr)):
        print(arr[i])

Insert_element()

# 3.Extend it is used for Joining one Array with another array
# syntax: extend(another_array)

def Extend_element():
    arr = [10,20,30,40]
    print('The elements in array are:')
    for i in range(len(arr)):
        print(arr[i])
    new_array = [50,60,70]
    arr.extend(new_array)
    print('Now the current elements in array is:')
    for i in range(len(arr)):
        print(arr[i])

Extend_element()

# 4.Remove it is used to remove any other elements in your desired location
# syntax: remove(value)

def remove_element():
    arr = [1,2,3,4]
    print('The elements in array are:')
    for i in range(len(arr)):
        print(arr[i])
    arr.remove(3)
    print('Current element is:')
    for i in range(len(arr)):
        print(arr[i])

remove_element()

# 5.pop it is used to remove the last element in an array

def remove_last_element():
    arr = [1,2,3,4]
    print('The elements in array are:')
    for i in range(len(arr)):
        print(arr[i])
    arr.pop()
    print('The current elements in array is:')
    for i in range(len(arr)):
        print(arr[i])

remove_last_element()

# 6.reverse it is used to reverse a element in an array

def reverse_element():
    arr = [1,2,3,4]
    print('The elements in array are:')
    for i in range(len(arr)):
        print(arr[i])
    arr.reverse()
    print('The current elements in array is:')
    for i in range(len(arr)):
        print(arr[i])

reverse_element()

# 7.Count it is used to count a number of times the particular element appears in an array using count() function
# syntax: array.count(value)

def Count_element():
    arr = [1,2,3,5,3,4,5,6,6,3,5]
    print('The elements in array are:')
    for i in range(len(arr)):
        print(arr[i])
    print('The Count of 6 is:',arr.count(6))

Count_element()

""" Two Pointer Technique in Array """

# Reverse an array
array = [1,2,3,4,5]
left = 0
right = len(array) - 1

def reverse_array(array,left,right):
  while left < right:
    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    left +=1
    right -=1

reverse_array(array,left,right)
print('Reversed array:',array)

# find a palindrome

word = input('Enter a word:')

def is_palindrome(s):
    left = 0
    right = len(word)-1
    while left < right:
        if s[left] != s[right]:
            print(s,'is not a palindrome')
            return
        left +=1
        right -=1
    print(s,'is a palindrome')

is_palindrome(word)








