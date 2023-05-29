import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
# node = [i+1 for i in range(N)]
indegree = [0] * (N+1)
graph = [[] for _ in range (N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
# print(graph)
print(indegree)
def topology_sort():
    result = []
    queue = deque()
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

