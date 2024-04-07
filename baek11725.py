import sys
sys.setrecursionlimit(10 ** 8)
n = int(sys.stdin.readline())
graph = [[] for i in range (n+1)]
visited = [0 for _ in range (n+1)]
for i in range (n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    for x in graph[v]:
        if visited[x] == 0:
            visited[x] = v
            dfs(x)
dfs(1)
for i in range (2,n+1):
    print(visited[i])