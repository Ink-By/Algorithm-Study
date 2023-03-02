import sys
firstinput = list(sys.stdin.readline().rstrip())

N = len(firstinput)
M = int(sys.stdin.readline())
cursor = N
for _ in range(M):
    order = sys.stdin.readline().split()
    if (order[0] == 'D'):
        if (cursor != N):
            cursor += 1
    elif (order[0] == 'L'):
        if (cursor != 0):
            cursor -= 1
    elif (order[0] == 'B'):
        if (cursor != 0):

            del firstinput[cursor-1]
            cursor -= 1
            # 삭제하고 나면 커서도 1 줄어듬

    elif (order[0] == 'P'):
        # print(order[1])
        firstinput.insert(cursor, order[1])
        cursor += 1
Result = ''
for i in (firstinput):
    Result += i
print(Result)
