inputA = input()
inputA = inputA.upper()#65 90

number = [0]*26
for i in inputA:
    number[ord(i)-65] += 1
    
flag = 1
if 0 in number:
    flag = 0

if (flag == 0):
    print("NO")
else:
    print("YES")