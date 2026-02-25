sub1 = int(input("Enter tamil mark:"))
sub2 = int(input("Enter english mark:"))
sub3 = int(input("Enter maths mark:"))
sub4 = int(input("Enter science mark:"))
sub5 = int(input("Enter social science mark:"))

average = (sub1+sub2+sub3+sub4+sub5)/5


if(average<35):
    print("Additional class is required")
else:
    print("You are good to go")