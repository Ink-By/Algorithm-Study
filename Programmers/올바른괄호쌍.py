a = list(input())
stack = []
flag = "YES"
for g in a:
    if g == '(':
        stack.append(g)
    if g == ')':
        if stack:
            stack.pop()
        else:
            flag = "NO"
            break
if stack or flag == "NO":
    print("NO")
else:
    print("YES")