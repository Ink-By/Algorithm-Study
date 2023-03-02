import sys
N, M = map(int, sys.stdin.readline().split())
A = [[0 for i in range(M)] for j in range(N)]
A[0][0] = 1

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))

    for j in range(M):
        A[i][j] = a[j]


B_N, B_M = map(int, sys.stdin.readline().split())
B = [[0 for i in range(B_M)] for j in range(B_N)]
for i in range(B_N):
    b = list(map(int, sys.stdin.readline().split()))
    for j in range(B_M):
        B[i][j] = b[j]

result = [[0 for i in range(B_M)] for j in range(N)]
j = 0
for x in range(N):
    for y in range(B_M):
        for z in range(M):
            result[x][y] += A[x][z] * B[z][y]
for i in result:
    for j in i:
        print(j, end=" ")
    print()
