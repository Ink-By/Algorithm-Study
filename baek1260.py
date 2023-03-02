import sys
N,M,V = map(int, input().split())
graph = [[]for i in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
def DFS(v):
    print(v,end=" ")
    visited[v] = 1
    for x in graph[v]:
        if visited[x] == 0:
            DFS(x)
def BFS(v):
    
DFS(V)
