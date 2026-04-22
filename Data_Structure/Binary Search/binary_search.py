# Binary Search algorithm
arr = [2,7,8,10,12]
start = 0
end = len(arr)-1
target = 12
while(start <= end):
    mid_index = (start + end)//2
    if(arr[mid_index] == target):
        print(f'Number found at index:',mid_index)
        break
    elif(arr[mid_index] < target):
        start = mid_index + 1
    elif(arr[mid_index] > target):
        end = mid_index - 1