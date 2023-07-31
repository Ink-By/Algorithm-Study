testcase = int(input())
for _ in range (testcase):
    a,b = map(int,input().split())
    code = input()
    if(_<testcase-1):
        input()
    count = 0
    flag = "YES"
    start = False
    for i in code:
        if i == 'O':
            if start:
                if count > b:
                    flag = "NO"
                    break
            else:
                start = True
        elif i == '@':
            if start:
                if count > b:
                    flag = "NO"
                    break
            else:
                start = True
        if i == '#' and start:
            count += 1
    print(flag)