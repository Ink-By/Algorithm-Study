import sys
A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.reverse()
ten = 0
for i in range(m):
    ten += arr[i]*(A**i)

result = []
while (ten//B != 0):
    result.append(ten % B)
    ten = ten//B
result.append(ten)
result.reverse()

print(" ".join(map(str, result)))
