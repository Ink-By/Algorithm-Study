import sys
A_,P = map(int, sys.stdin.readline().split())
A = str(A_)

D = [A]
D_sum = 0
k=0
while(True):
    # if(len(D)==20):
    #     break
    save = D[k]
    
    D_sum = 0
    for i in range (len(save)):
        D_sum += int(save[i])**P
    # print(D_sum)
    if str(D_sum) in D:
        break
    D.append(str(D_sum))
    k+=1
cnt = 0
for i in D:
    if(i == str(D_sum)):
        break
    cnt+=1
print(cnt)