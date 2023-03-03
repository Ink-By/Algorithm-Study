import sys
N,M = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))
height.sort()

start = 1
end = height[-1]
while start <= end:
    mid = (start+end) //2
    count = 0
    for i in height:
        if i >= mid:
            count += i - mid
    if count >= M :
        start = mid +1
    else:
        end = mid - 1
print(end)