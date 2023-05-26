import sys
A_, P = map(int, sys.stdin.readline().split())
visited = [0]*90000


def DFS(n):
    visited[n] += 1
    if (visited[n] == 3):
        return
    sum_ = 0
    while (n):
        sum_ += (int)((n % 10)**P)
        n /= 10
    DFS(sum_)


DFS(A_)
result = 0
for i in range(90000):
    if (visited[i] == 1):
        result += 1
print(result)
