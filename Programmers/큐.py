from collections import deque
a = int(input())
que = deque()
for _ in range (a):
    a = list (map(int, input().split()))
    if a[0]==1:
        que.append(a[1])
    elif a[0] == 2:
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif a[0] == 3:
        print(len(que))
    elif a[0] == 4:
        if que:
            print(0)
        else:
            print(1)
    else:
        if que:
            print(-1)
        else:
            print(que.appendleft(que.popleft()))