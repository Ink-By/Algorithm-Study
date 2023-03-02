import sys
N, M = map(int, sys.stdin.readline().split())

s = []
a = list(map(int, sys.stdin.readline().split()))
a.sort()

def dfs():
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(0, N):
        s.append(a[i])
        dfs()
        s.pop()


dfs()
