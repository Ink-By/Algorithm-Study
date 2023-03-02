import sys
from collections import deque
testcase = int(sys.stdin.readline())
for i in range(testcase):

    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    if (n == 0):
        queue = deque()
    flag = 0
    countR = 0
    for j in (p):
        if (j == 'R'):
            countR += 1
        else:
            if (len(queue) == 0):
                print("error")
                flag = 1
                break
            else:
                if (countR % 2 == 0):
                    queue.popleft()
                else:
                    queue.pop()
    if (flag == 0):
        if (countR % 2 == 0):
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")
