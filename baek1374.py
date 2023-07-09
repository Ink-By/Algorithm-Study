import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range (N):
    num, start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,[start,end,num])

start, end, num = heapq.heappop(heap)
heapq.heappush()
