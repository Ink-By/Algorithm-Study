import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split()))for _ in range (n)]
visited = [[-1]* m for _ in range(n)]
count = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs (arr,a,b):
    que = deque([(a,b)])
    arr[a][b] = 0
    count = 1
    while que:
        x_,y_ = que.popleft()
        for i in range (4):
            x = dx[i] + x_
            y = dy[i] + y_
            if 0<=x<n and 0<=y<m:
                if arr[x][y] == 0:
                    visited[x][y] = 0
                elif arr[x][y] == 1:
                    arr[x][y] = 0
                    que.append((x,y))
                    count+=1
    return count
size = []
for i in range(n):
    for j in range (m):
        if arr[i][j] == 1:
            size.append(bfs(arr,i,j))
if len(size) == 0:
    print(len(size))
    print(0)
else:
    print(len(size))
    print(max(size))