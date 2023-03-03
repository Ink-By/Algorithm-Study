import sys
case = int(sys.stdin.readline())

k = 10000
sosu = [False, False] + [True]*(k-1)
primes = []
for i in range(2, k+1):
    if (sosu[i]):
        primes.append(i)
        for j in range(2*i, k+1, i):
            sosu[j] = False


for i in range(case):
    a = int(sys.stdin.readline())
    half = a//2
    while (True):
        if half in (primes):
            if (a-half) in (primes):
                break
            else:
                half -= 1
        else:
            half -= 1
    print(half, a-half)
