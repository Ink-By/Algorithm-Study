import sys
from collections import deque
testcase = int(sys.stdin.readline())
for _ in range (testcase):
    N, M = map(int,sys.stdin.readline().split())
    listque = deque(list(map(int,sys.stdin.readline().split())))
    count = 0
    save = listque[M]
    while(True):
        maxindex = max(listque)
        M -= 1
        a= listque.popleft()
        if(maxindex == a):
            count += 1
            if(M<0):
                print(count)
                break
        else:
            listque.append(a)
            if(M<0):
                M = len(listque)-1

