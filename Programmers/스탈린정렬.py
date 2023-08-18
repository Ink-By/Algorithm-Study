test = int(input())
for _ in range (test):
    length = int(input())
    a =list( map(int,input().split()))
    stack = []
    for i in a:
        if stack:
            if stack[-1]<i:
                stack.append(i)
        else:
            stack.append(i)
    for result in stack:
        print(result,end=" ")