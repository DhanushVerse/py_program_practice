# / reverse string

def reverse_string(s):
    return s[::-1]
print(reverse_string("developer"))

# remove duplicates


def remove_duplicates(my_list):
    unique_list = set(my_list)
    return list(unique_list)
numbers = [10,20,10,30,40,20]
print(remove_duplicates(numbers))



# even or odd

def find_even(numbers):
    even_numbers = []
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
    return even_numbers
    
num = [2,4,3,7,8,9]
print(find_even(num))

# factorial of a number


name = ["developer","python","code"]
name.extend(["java","c++"])
name.extend(["html"])
print(name)






