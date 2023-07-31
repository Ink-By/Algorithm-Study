a = input()
b = input()
arrb = []
for i in b:
    arrb.append(i)
for i in range (len(a)):
    flag = "NO"
    for j in range(len(arrb)):
        if(a[i] == arrb[j]):
            flag = "YES"
            arrb[j] = '0'
            break
    if(flag == "NO"):
        break
print(flag)