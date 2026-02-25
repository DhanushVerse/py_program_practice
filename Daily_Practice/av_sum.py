a = []
for i in range(5):
    num = int(input("Enter num:"))
    a.append(num)
print(a)

sum = 0
for i in a:
    sum = sum+i
print("sum:",sum)
print("avg:",sum/5)
