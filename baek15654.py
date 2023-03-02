import sys
N, M = map(int, sys.stdin.readline().split())

s = []
a = list(map(int, sys.stdin.readline().split()))
a.sort()


def dfs():
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(N):
        if a[i] not in s:
            s.append(a[i])
            dfs()
            s.pop()


dfs()
