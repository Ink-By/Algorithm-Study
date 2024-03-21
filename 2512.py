import sys
n = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
if sum(request) <= m :
    print(max(request))
else:
    