import sys
N, M = map(int, sys.stdin.readline().split())
s = []
visited = [False]*(N+1)


def dfs(k):
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(k,N+1):
        if (visited[i]):
            continue
        visited[i] = True
        s.append(i)
        dfs(i+1)
        s.pop()
        visited[i] = False
        # visited[i] = False
dfs(1)
