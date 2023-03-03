import sys


def find(x):
    if (x == graph[x]):
        return x
    graph[x] = find(graph[x])
    return graph[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if (a == b):
        return
    elif (a > b):
        graph[a] = b
    else:
        graph[b] = a
    return


N, M = map(int, sys.stdin.readline().split())
graph = [i for i in range(N)]
result = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a = find(a)
    b = find(b)
    if (a == b):
        result = i+1
        break
    union(a, b)
print(result)
