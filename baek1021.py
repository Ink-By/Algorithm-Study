import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
queue = deque(i for i in range(N))


D = list(map(int, sys.stdin.readline().split()))

count = 0
# print(queue)
for i in D:
    flag = "r"
    i = i-1
    if (i == queue[0]):
        queue.popleft()
    else:
        k = 0
        if (len(queue) % 2 == 1):
            k = len(queue)//2+1
        else:
            k = len(queue)//2
        for j in range(0, k):

            if (i == queue[j]):
                # print(i, " ", queue[j])
                flag = "l"

        while (True):
            # print(queue, " ", flag, count)
            if (i == queue[0]):
                queue.popleft()
                break
            if (flag == "l"):
                queue.append(queue.popleft())
                count += 1
            else:
                queue.appendleft(queue.pop())
                count += 1
    # print(queue , count)
print(count)
