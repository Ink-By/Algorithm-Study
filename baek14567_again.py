import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]
degree = [0] * (N+1) 
for i in range (M):
    a,b = map(int,sys.stdin.readline().split())
    degree[b]+=1
    graph[a].append(b)

queue = deque()
result = [0 for _ in range (N+1)]
for i in range (1,N+1):
    if(degree[i] == 0):
        queue.append((i,1))
        result[i] = 1
while queue:
    a, count = queue.popleft()
    for i in graph[a]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append((i,count+1))
            result[i] = count + 1
for i in range (1,N+1):
    print(result[i],end = " ")