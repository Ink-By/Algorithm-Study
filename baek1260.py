import sys
from collections import deque
N, M, V = map(int, input().split())
graph = [[]for i in range(N+1)]
visited = [0]*(N+1)

dfsResult = []
bfsResult = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
    
    graph[a].sort()
    graph[b].sort()


def DFS(v):
    dfsResult.append(str(v))
    visited[v] = 1
    for x in graph[v]:
        if visited[x] == 0:
            DFS(x)


def BFS(graph, node, visited):
    queue = deque([node])
    visited[node] = 1
    while queue:
        v = queue.popleft()
        bfsResult.append(str(v))

        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = 1


DFS(V)
visited = [0]*(N+1)
BFS(graph, V, visited)

print(" ".join(dfsResult))
print(" ".join(bfsResult))
