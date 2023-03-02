import sys


def dfs():
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return

    for k in range(len(a_set)):
        if not (visited[k] == 0):
            visited[k] -= 1
            s.append(a_set[k])
            dfs()
            s.pop()
            visited[k] += 1


N, M = map(int, sys.stdin.readline().split())
s = []
a = list(map(int, sys.stdin.readline().split()))
a_set = list(set(a))
a_set.sort()
visited = [0]*(len(a_set))
result = []
for i in range(len(a_set)):
    visited[i] = a.count(a_set[i])

dfs()
