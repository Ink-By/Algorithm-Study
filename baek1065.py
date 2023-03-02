import sys
a = int(sys.stdin.readline())
result = 0
for i in range (1 , a+1):
    if(i<100):
        result += 1
    else:
        temp = list(map(int,str(i)))
        if(temp[1]-temp[0]==temp[2]-temp[1]):
            result+=1
print(result)