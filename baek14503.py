import sys
N, Q = map(int, sys.stdin.readline().split())
count = 1
r, c, d = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(N)]

for i in range(N):
    arr[i] = (list(map(int, sys.stdin.readline().split())))
while (True):
    if (arr[r][c-1] == 1 and arr[r+1][c] == 1 and arr[r][c+1] == 1 and arr[r-1][c] == 1):
        if (d == 0):
            if (r+1 != N-1):
                r += 1
            else:
                break
        elif (d == 3):
            if (c+1 != Q-1):
                c += 1
            else:
                break
        elif (d == 2):
            if (r-1 != 0):
                r -= 1
            else:
                break

        elif (d == 1):
            if (c-1 != 0):
                c -= 1
            else:
                break

    elif (d == 0):
        if (arr[r][c-1] == 1):
            d = 3
        else:

            d = 3
            c = c-1
            count += 1
            arr[r][c] = 1
    elif (d == 3):
        if (arr[r+1][c] == 1):
            d = 2
        else:
            d = 2
            r = r+1
            count += 1
            arr[r][c] = 1
    elif (d == 2):
        if (arr[r][c+1] == 1):
            d = 1
        else:
            d = 1
            c = c+1
            count += 1
            arr[r][c] = 1
    elif (d == 1):
        if (arr[r-1][c] == 1):
            d = 0
        else:
            d = 0
            r = r-1
            count += 1
            arr[r][c] = 1


print(count)
