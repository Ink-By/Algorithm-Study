import sys
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
arr = []
sum = 0
for i in a:
    sum += i
    arr.append(sum)
for _ in range (m):
    start, end = map(int,sys.stdin.readline().split())
    start-=1
    end-=1
    if start==0:
        print(arr[end])
    else:
        print(arr[end]-arr[start-1])
