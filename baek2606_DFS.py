import sys
computer = int(sys.stdin.readline())
pair_count = int(sys.stdin.readline())

graph = [[] for i in range(computer+1)]
visited = [0]*(computer+1)

for i in range(pair_count):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(v):
    visited[v] = 1
    for x in graph[v]:
        if visited[x] == 0:
            dfs(x)


dfs(1)
print(sum(visited)-1)
