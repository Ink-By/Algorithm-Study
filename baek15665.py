import sys


def dfs():
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return

    for k in range(len(a_set)):
        s.append(a_set[k])
        dfs()
        s.pop()


N, M = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
a_set = list(set(a))
a_set.sort()
visited = [0]*(len(a_set))
s = []
for i in range(len(a_set)):
    visited[i] = a.count(a_set[i])
    if (visited[i] == 1):
        visited[i] += 1

dfs()
