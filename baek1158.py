import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
que = deque(list(i for i in range(1, N+1)))
count = 1
resultArr = []
while (que):
    if (count == K):
        resultArr.append(str(que.popleft()))
        count = 1
    else:
        que.append(str(que.popleft()))
        count += 1

print("<", end="")
print(", ".join(resultArr), end=">")
