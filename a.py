def solver(N,A):
    if(A.count(1)==1):
        for i in (len(A)):
            if(A[i]==1):
                A[i]=0
    elif(A[N//2]==1):
        A[N//2]=0
    subsets=[[]]
    for i in range(len(A)):
        L = len(subsets)
        for j in range(i+1,len(A)+1):
            subsets.append(A[i:j])
    countZero = 0
    # for 0 in (subsets):

    return subsets
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    out = solver(N,A)
    print(out)