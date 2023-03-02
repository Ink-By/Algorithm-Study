import sys
x,y,w,h = map(int,sys.stdin.readline().split())
#4개차이 구해서 4개중 가장 작은 min 출력
a = w-x
b = h-y

c = min(x,a)
d = min(y,b)
result = min(c,d)
print(result)