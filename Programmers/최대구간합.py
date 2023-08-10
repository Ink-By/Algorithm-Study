a = int(input())

arr = list(map(int, input().split()))
sum = 0
history = []
for i in arr:
    sum +=i 
    history.append(sum)
result = -9999
for i in range(a):
    
