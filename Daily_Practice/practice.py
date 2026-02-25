# calculation of square numbers

def square_num(num):
    num = int(input("Enter a number:"))
    result = num * num 
    print(f'Square of {num} is:',result)

square_num(sum)

# length of a string

def len_str():
    string = input("Enter a string:")
    length = len(string)
    print(f'length of a string is:',length)

len_str()

# fing number of vowels in a given string

def vowel_str():
    string = input("Enter a string:")
    vowel_count = 0
    for i in string:
        if((i=='a' or i=='e' or i=='i' or i=='o' or i=='u')
        or((i=='A' or i=='E' or i=='I' or i=='O' or i=='U'))):
            vowel_count+=1
    print(f'The number of vowels in string is:',vowel_count)

vowel_str()

# so i have a problem in making conditions

# program for count number of digits and letter in a string

def digit_letter_counter():
    string = input('Enter some string:')
    digit_counter = 0
    letter_counter = 0
    for i in string:
        if(i.isdigit()):
            digit_counter+=1
        else:
            letter_counter+=1
    print(f'The Number of digits in a string are:',digit_counter)
    print(f'The Number of letters in a string are:',letter_counter)

    # i learn today is if you want some count first initialize a variable to assign a value 0 and later we update it
    # use inbuilt methods sometimes for reduce time

digit_letter_counter()   