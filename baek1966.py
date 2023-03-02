import sys
from queue import PriorityQueue
testcase = int(sys.stdin.readline())
for i in range(testcase):
    N, M = map(int, sys.stdin.readline().split())
    # 숫자 클수록 우선도 높음
    count = 0
    que = PriorityQueue(maxsize=N)
    arr = list(map(int, sys.stdin.readline().split()))
    for j in arr:
        que.put(((-1)*j,j))
    while (True):
        k = que.get()[1]
        print(k)
        if (k == arr[M]):
            count += 1
            break

        count += 1
    print(count)
