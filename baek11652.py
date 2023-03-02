import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
counter = Counter(arr).most_common(1)


print(counter[0][0])
