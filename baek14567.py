import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
indegree = [0] * (N+1)
graph = [[] for _ in range (N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
for i in range (len(graph)):
    print(graph[i])
def topology_sort():
    result = []
    queue = deque()
    print(indegree)
    for i in range (1,N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)
        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=" ")
topology_sort()

