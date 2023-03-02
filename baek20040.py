import sys


def find(x):
    if x == graph[x]:
        return x
    graph[x] = find(graph[x])
    return graph[x]


def union(a_x, b_x):
    a_x = find(a_x)
    b_x = find(b_x)
    if a_x == b_x:
        return
    if a_x < b_x:
        graph[b_x] = a_x
    elif a_x > b_x:
        graph[a_x] = b_x
    return


N, M = map(int, sys.stdin.readline().split())
graph = list(i for i in range(N))
result = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a = find(a)
    b = find(b)
    if a == b:
        result = i+1
        break
    union(a, b)
print(result)
