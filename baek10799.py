import sys
layzorCount = 0
Count = 0
stack = []
inputs  = sys.stdin.readline().rstrip()

for i in range(len(inputs)):
    if(inputs[i]=='('):
        if(inputs[i+1]==')'):
            # layzorCount += 1
            if(len(stack)!=0):
                Count += len(stack)
        else:
            Count += 1
            stack.append('(')
    elif(inputs[i-1]!='(' and inputs[i]==')'):
        
        stack.pop()
print(Count)
