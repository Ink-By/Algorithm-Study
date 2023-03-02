import sys
from collections import Counter
a,b = map(int,sys.stdin.readline().split())
data = []
for i in range (a):
    data.append(sys.stdin.readline())
s1 = set(data)
test = []
for i in range (b):
    test.append(sys.stdin.readline())
count = Counter(test)
s2 = set(test)
result = s1 & s2
answer=0
for people, counts in count.items():
    for a in result:
        if(people==a):
            answer += counts
print(answer)


