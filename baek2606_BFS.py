import sys
from collections import deque
computer = int(sys.stdin.readline())
pair_count = int(sys.stdin.readline())

graph = [[] for i in range (computer+1)]
visited = [0]*(computer+1)

for i in range(pair_count):
    a,b = map(int,sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
visited[1] = 1
Queue = deque([1])
while Queue:
    temp = Queue.popleft()
    for x in graph[temp]:
        if visited[x] == 0:
            Queue.append(x)
            visited[x] = 1
print(sum(visited)-1)