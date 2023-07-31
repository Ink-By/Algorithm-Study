import sys
from collections import deque
test = int(sys.stdin.readline())
arr = [0] * (test+1)
graph = [[] for _ in range (test+1)]
time = [0] *(test+1)
for i in range (test):
    data = list(map(int,sys.stdin.readline().split()))
    time[i] = data[0]
    building = data[1:]
    for j in building:
        graph[j].append(i)
        arr[i]+=1
    #차수 연결
def sort():
    result = [0] * (test+1)
    queue = deque()
    for i in range (1,test+1):
        if arr[i] ==0:
            queue.append(i)
    while queue:
        t = queue.popleft()
        result[t] += time[t]
        for j in graph[t]:
            arr[j] -= 1
            result[j] = max(result[j],result[t])
            if arr[j] ==  0:
                queue.append(j)
    return result
r = sort()
for i in range (1,test+1):
    print(r[i])