import heapq
import sys
a = int(sys.stdin.readline())
que = []

for i in range(a):
    card = (int(sys.stdin.readline()))
    heapq.heappush(que, card)
result = []
if (a == 1):
    print(0)
else:

    while (len(que) > 1):
        temp1 = heapq.heappop(que)
        temp2 = heapq.heappop(que)
        result.append(temp1+temp2)
        heapq.heappush(que, temp1+temp2)
    print(sum(result))
