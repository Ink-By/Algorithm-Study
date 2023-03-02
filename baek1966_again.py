import sys
from collections import deque
testcase = int(sys.stdin.readline())
for i in range(testcase):
    N, M = map(int, sys.stdin.readline().split())
    # 숫자 클수록 우선도 높음
    count = 0
    que = deque(list(map(int, sys.stdin.readline().split())))
    while (True):
        maxindex = max(que)

        a = que.popleft()
        M -= 1
        if maxindex == a:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            que.append(a)
            if M < 0:
                M = len(que)-1
