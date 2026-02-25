# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# op = input("Enter the operation you perform:")

# if(op == "add"):
#     print(a+b)
# elif(op == "sub"):
#     print(a-b)
# elif(op == "mul"):
#     print(a*b)
# elif(op == "div"):
#     print(a/b)

scorepercentage = int(input("Enter a score percentage:"))
if(scorepercentage > 70):
    name = input("Enter your name:")
    department = input("Enter your department:")
    location = input("Enter your location:")
    print("Your are eligible")
else:
    print("You are not eligible")