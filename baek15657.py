import sys
N, M = map(int, sys.stdin.readline().split())

s = []
a = list(map(int, sys.stdin.readline().split()))
a.sort()


def dfs(x):
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(x, N):
        s.append(a[i])
        dfs(i)
        s.pop()


dfs(0)
