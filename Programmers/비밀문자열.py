a = input()
b = input()
k = 0
flag = "NO"
for j in range (len(b)):
    flag = "NO"
    if(k>=len(a)-1):
        flag = "NO"
        break
    for i in range (k,len(a)):
        # print(a[i],b[j])
        k+=1
        if(a[i] == b[j]):
            flag = "YES"
            
            break
        
    if(flag == "NO"):
        break
print(flag)