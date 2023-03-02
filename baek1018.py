import sys
N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline())

result = []

for i in range(N-7):
    for j in range(M-7):
        drawB = 0
        drawW = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if (board[a][b] != 'B'):
                        drawB += 1
                    else:
                        drawW += 1
                else:
                    if (board[a][b] != 'B'):
                        drawW += 1
                    else:
                        drawB += 1
        result.append(drawB)
        result.append(drawW)

print(min(result))
