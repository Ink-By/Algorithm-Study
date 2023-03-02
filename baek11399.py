import sys
people = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
count = [0]*people
for i in range (people):
    for j in range(i+1):
        count[i]+=a[j]

print(sum(count) )