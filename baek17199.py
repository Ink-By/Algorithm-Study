import sys
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
dp = [0]
temp = 0
for i in num:
    temp += i
    dp.append(temp)


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b]-dp[a-1])
