import sys
computer = int(sys.stdin.readline())
pair = int(sys.stdin.readline())
graph = [[]for i in range(computer + 1)]
visit = [0] * (computer + 1)
for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(v):  # DFS사용
    visit[v] = 1
    for k in graph[v]:
        if (visit[k] == 0):
            dfs(k)


dfs(1)
print(sum(visit)-1)
