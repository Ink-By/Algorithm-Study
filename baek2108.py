import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()

result1 = round(sum(num)/N)
result2 = num[N//2]
result3 = 0
result4 = num[N-1]-num[0]

counter = Counter(num).most_common(2)
if N > 1:
    if (counter[0][1] == counter[1][1]):
        result3 = counter[1][0]
    else:
        result3 = counter[0][0]

else:
    result3 = counter[0][0]

print(result1)
print(result2)
print(result3)
print(result4)
