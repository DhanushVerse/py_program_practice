# # Binary Search algorithm
# arr = [2,7,8,10,12]
# start = 0
# end = len(arr)-1
# target = 12
# while(start <= end):
#     mid_index = (start + end)//2
#     if(arr[mid_index] == target):
#         print(f'Number found at index:',mid_index)
#         break
#     elif(arr[mid_index] < target):
#         start = mid_index + 1
#     elif(arr[mid_index] > target):
#         end = mid_index - 1

# Two sum problem
arr1 = [2,7,11,15]
start = 0
end = len(arr1)-1
target = 9
while(start <= end):
    mid = arr1[start] + arr1[end]
    if(mid == target):
        print(f'Number Index:',start,end)
        break
    elif(mid > target):
        end = end-1
    else:
        start +=1