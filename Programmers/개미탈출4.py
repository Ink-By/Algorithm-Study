testcase = int(input())
for _ in range(testcase):
    a, b = map(int, input().split())
    code = input()
    arr = [i for i in code]
    atk, hp = map(int, input().split())
    Matk, Mhp = map(int, input().split())
    LocationOFjun = arr.index('@')
    LocationOFO = []
    count = 0   
    # 싸워서 지는지 안지는지
    if _ < testcase - 1:
        input()
    flag = "YES"
    count = 0
    start = False
    index = LocationOFjun
    if 'O' in (arr[0:LocationOFjun+1]):
        
        while(True):
            if arr[index] == 'O':
                LocationOFO.append(index)
                break
            index-=1  
    index = LocationOFjun
    if 'O' in (arr[LocationOFjun:len(arr)]):
        # LocationOFO.append(arr[LocationOFjun:len(arr)].index('O'))  
        while(True):
            if arr[index] == 'O':
                LocationOFO.append(index)
                break
            index+=1    
    
    while(True):
        Mhp -= atk
        
        if Mhp <= 0:
            flag = "YES"
            break
        hp -= Matk
        if hp <= 0:
            flag = "NO"
            break
    # print(flag)
    if flag=="YES":
        
        for i in range (len(LocationOFO)):
            flag = "NO"
            count = 0
            if LocationOFO[i]<LocationOFjun:
                for k in arr[LocationOFO[i]:LocationOFjun+1]:
                    if k == '#':
                        count+=1
            else:
                for k in arr[LocationOFjun:LocationOFO[i]+1]:
                    if k == '#':
                        count+=1
            # print(flag)
            if count<=b:
                flag = "YES"
                break
    else:
        for i in range (len(LocationOFO)):
            count = 0
            flag = "YES"
            if LocationOFO[i]<LocationOFjun:
                for k in arr[LocationOFO[i]:LocationOFjun+1]:
                    if k == '#':
                        count+=1
                    if k == '&':
                        flag = "NO"
                        break
            else:
                for k in arr[LocationOFjun:LocationOFO[i]+1]:
                    if k == '#':
                        count+=1
                    if k == '&':
                        flag = "NO"
                        break
            if count <= b and flag == "YES":
                flag = "YES"
                break
            else:
                flag = "NO"
    print(flag)
