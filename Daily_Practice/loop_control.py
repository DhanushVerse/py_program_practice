# number_list = [10, 25, 4, 99, 120, 50]
# for num in number_list:
#     if num == 99:
#         print('Found it')
#         break
#     elif num < 10:
#         continue
#     print(num)

# for i in range(1,11):     # range means counting a numbers or repeatate the loop
#     if i % 2 == 0:
#         print(i)


for i in range(1,21):
    if i == 15:
        print('Target Reached')
        break
    elif i % 2 != 0:
        continue
    print(i)

