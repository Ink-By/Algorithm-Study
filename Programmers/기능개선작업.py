def solution(progresses, speeds):
    arr = []
                
    answer = []
    for i in range(len(progresses)):
        percent = 100 - progresses[i]
        if(percent % speeds[i] > 0):
            arr.append(percent//speeds[i] + 1)    
        else :
            arr.append(percent//speeds[i])
    for i in range (len(arr)):
        for j in range (0,i):
            if(arr[j] > arr[i]):
                arr[i] = arr[j]
    count = 0
    for i in range (len(arr)):
        if (i == 0):
            count += 1
        else:
            if(arr[i]== arr[i-1]):
                count +=1
                if(i==len(arr)-1):
                    answer.append(count)

            else:
                answer.append(count)
                count = 1
                if(i==len(arr)-1):
                    answer.append(count)

    return answer

p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
print(solution(p,s))