import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range (m):
    graph.append(list(sys.stdin.readline()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
strength = [0,0]
def bfs (x,y,team):
    queue = deque()
    queue.append((x,y))
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range (4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0<=_x<n and 0<= _y<m:
                if graph[_x][_y] == team:
                    graph[_x][_y] -= 1
                    queue.append((_x,_y))
                    count +=1
    return count*count

for i in range (m):
    for j in range(n):
        if graph[i][j] == "W":
            strength[0] += bfs[i,j,"W"]
        else:
            strength[1] += bfs[i,j,"B"]
print(" ".join(map(str,strength)))