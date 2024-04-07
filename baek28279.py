import sys
from collections import deque
n = int(sys.stdin.readline())
arr = deque()
for i in range (n):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        arr.appendleft(command[1])
    elif command[0] == 2:
        arr.append(command[1])
    elif command[0] == 3:
        if len(arr) ==0:
            print(-1)
        else:
            print(arr.popleft())
    elif command[0] == 4:
        if len(arr) ==0:
            print(-1)
        else:
            print(arr.pop())
    elif command[0] == 5:
        print(len(arr))
    elif command[0] == 6:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 7:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])