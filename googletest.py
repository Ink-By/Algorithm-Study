def Solve (N, A):
    if 0 in A:
        return 0
    arrpos = []
    arrneg = []
    for i in A:
        if(i>0):
            arrpos.append(i)
        else:
            arrneg.append(i)
    savepos = min(arrpos)
    saveneg = max(arrneg)
    if(savepos-saveneg<100):
        return saveneg
    else:
        return savepos
    # Write your code here
    
N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print (out_)