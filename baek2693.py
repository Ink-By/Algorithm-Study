import sys
t = int(sys.stdin.readline())
for i in range (t):
    arr = list(map(int,sys.stdin.readline().split()))
    arr.sort()
    print(arr[-3])