import sys
N, M = map(int, sys.stdin.readline().split())
s = []


def dfs(x):
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(x, N+1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)
