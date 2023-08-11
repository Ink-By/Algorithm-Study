a,b = map(int,input().split())
s = input()
arr = []
sum = 0
for i in range (a):
    if s[i] == 'e':
        sum+=1
    arr.append(sum)
for _ in range (b):
    l,r = map(int,input().split())
    if l==r:
        if r==1:
            print(arr[r-1])
        else:
            print(arr[r-1]-arr[r-2])
    else:
        if l==1:
            print(arr[r-1])
        else:
            print(arr[r-1]- arr[l-2])