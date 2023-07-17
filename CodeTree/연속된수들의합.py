import sys
a = int(sys.stdin.readline())
arr = [i for i in range (1,a+2)]
start = 0
end = 1
count = 0
total = sum(arr[start:end])
end += 1
while(end<a+2):
    
    if(total < a):
        total += arr[end-1]
        end+=1
    elif(total > a):
        total -= arr[start]
        start += 1
    else:
        total += arr[end-1]
        count+=1
        end+=1
    
    
    
print(count)