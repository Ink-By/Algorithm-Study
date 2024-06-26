import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range (n) ]
visited = [[-1] * m for _ in range (n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, b):
    que = deque([(a, b)])
    visited[a][b] = 0
    while que:
        x_,y_ = que.popleft()
        for p in range (4):
            x = x_ + dx[p]
            y = y_ + dy[p]
            if 0 <= x < n and 0 <= y < m:
                if visited[x][y] == -1:
                    if graph[x][y] == 1:
                        visited[x][y] = visited[x_][y_]+1
                        que.append((x,y))
                    elif graph[x][y] == 0:
                        visited[x][y] = 0

for i in range (n):
    for j in range (m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)
for i in range (n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0,end =" ")
        else:
            print(visited[i][j],end = " ")
    print()
