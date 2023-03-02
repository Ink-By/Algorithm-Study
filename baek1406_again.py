import sys
stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
N = len(stack1)
M = int(sys.stdin.readline())
cursor = N
for _ in range(M):
    order = sys.stdin.readline().split()
    if (order[0] == 'D'):
        if (stack2):
            stack1.append(stack2.pop())
    elif (order[0] == 'L'):
        if (stack1):
            stack2.append(stack1.pop())
    elif (order[0] == 'B'):
        if (stack1):
            stack1.pop()
            # 삭제하고 나면 커서도 1 줄어듬

    elif (order[0] == 'P'):
        # print(order[1])
        stack1.append(order[1])

print("".join(stack1+list(reversed(stack2))))
