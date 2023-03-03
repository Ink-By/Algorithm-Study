from collections import Counter
def func(n,k,a):
    count1 = Counter(a)
    for Number,counts in count1.items():
        print(Number,counts)

T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    out_1 = func(n,k,a)
    print(out_1)