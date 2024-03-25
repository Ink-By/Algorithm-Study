import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
dist = [[]for i in range (n+1)]
visited = [0] * (n+1)
def bfs(dist, i, visited):
    que = deque([i])
    visited[i] = 1
    while que:
        a = que.popleft()
        for i in dist[a]:
            if not (visited[i]):
                que.append(i)
                visited[i] = 1
for i in range (m):
    u, v = map(int, sys.stdin.readline().split())
    dist[u].append(v)
    dist[v].append(u)

result = 0
for i in range (1,n+1):
    if not visited[i]:
        bfs(dist,i,visited)
        result+=1


print(result)