def BinarySearch (arr,target):
    left = 0
    right = len(arr)-1
    while(True):
        mid = (left+right)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            left = mid+1
        else:
            right = mid-1
target = 7
arr = [0,1,2,3,4,5,6,7,8,9,10]
result = BinarySearch(arr,target)
print(result)