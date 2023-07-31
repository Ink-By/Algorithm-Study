testcase = int(input())
for _ in range(testcase):
    a, b = map(int, input().split())
    code = input()
    arr = [i for i in code]
    if _ < testcase - 1:
        input()
    flag = "YES"
    count = 0
    start = False
    locationOFblock = arr.index("G")
    locationOFjun = arr.index("@")
    locationOFgate = arr.index("O")
    if locationOFjun < locationOFblock:
        for i in arr[locationOFjun : locationOFblock + 1]:
            if i == "#":
                count += 1
    else:
        for i in arr[locationOFblock : locationOFjun + 1]:
            if i == "#":
                count += 1
    if count > b:
        count = 0
        if locationOFgate < locationOFjun:
            for i in arr[locationOFgate : locationOFjun + 1]:
                if i == "#":
                    count += 1
        else:
            for i in arr[locationOFjun : locationOFgate + 1]:
                if i == "#":
                    count += 1
        if count > b:
            flag = "NO"

    print(flag)
