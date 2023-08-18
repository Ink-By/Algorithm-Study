n = int(input())
stack = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        print(1 if not stack else 0)
    elif a[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
