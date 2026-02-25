# num = int(input("Enter a number:"))
# if(num%2==0):
#     print("The number",num,"is even")
# else:
#     print("The number",num,"is odd")

score = int(input("Enter a number:"))
if(score<35):
    print("Poor Student")
elif(score>35 and score<70):
    print("Average Student")
elif(score>70 and score<100):
    print("Good Student")
else:
    print("Invalid input")