import sys
from collections import deque
people = int(sys.stdin.readline())
graph = [[]for _ in range (people+1)]
while(True):
    a,b = map(int,sys.stdin.readline().split())
    if (a==-1 and b == -1):
        break
    graph[a].append(b)
    graph[b].append(a)
score = 10000
bosslist = []

def bfs(n):
    visited = [-1] * (people + 1)
    que = deque([n])
    visited[n] = 0
    while(que):
        a = que.popleft()
        for v in graph[a]:
            if visited[v]==-1:
                visited[v] = visited[a]+1
                que.append(v)
    return max(visited)
for i in range (1,people+1):
    tmp = bfs(i)
    if tmp < score:
        score = tmp
        bosslist = [i]
    elif tmp == score:
        bosslist.append(i)
print(score, len(bosslist))
print(" ".join(str(x) for x in bosslist))
