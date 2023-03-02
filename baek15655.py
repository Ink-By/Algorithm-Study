import sys
N, M = map(int, sys.stdin.readline().split())

s = []
a = list(map(int, sys.stdin.readline().split()))
a.sort()
visited = [False]*(N)


def dfs(x):
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(x, N):
        if (visited[i]):
            continue
        visited[i] = True

        s.append(a[i])
        x+=1
        dfs(x)
        s.pop()
        visited[i] = False


dfs(0)
