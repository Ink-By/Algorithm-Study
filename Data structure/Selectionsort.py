def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        minindex = i
        for j in range(i + 1, length):
            if arr[j] < arr[minindex]:
                minindex = j
        temp = arr[i]
        arr[i] = arr[minindex]
        arr[minindex] = temp
    return arr
arr = [10, 2, 3, 5, 9, 1, 4, 6, 8, 7]
print(selection_sort(arr))
