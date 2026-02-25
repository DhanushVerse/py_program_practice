def is_leap(year):
    if(year%4==0):  #leap
        if(year%100==0):  # not leap
            if(year%400==0):
                return True
            else:
                return False
        return True
    return False

year = int(input("Enter a year:"))
print(is_leap(year))