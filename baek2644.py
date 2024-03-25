import sys
n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for i in range (n+1)]
visited = [0 for i in range (n+1)]
result = []
def dfs(num, start):
    visited[start] = 1
    num += 1
    if (start == b):
        result.append(num)
        
    for i in graph[start]:
        if not visited[i]:
            dfs(num, i)

for i in range (m):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(0,a)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)