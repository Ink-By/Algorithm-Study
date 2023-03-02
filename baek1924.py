import sys
x,y = map(int,sys.stdin.readline().split())
DATE = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
calender = [[str(i) for i in range (32)] for j in range(13)]
dateCount = 0

for i in range (1,13):
    for j in range(1,32):
        save = dateCount
        
        if(dateCount==6):
            dateCount = 0
        else:
            dateCount += 1
        
        if(i == 1 or i == 3 or i== 5 or i == 7 or i ==8 or i==10 or i==12):
            # print(i,j,dateCount,DATE[save])
            calender[i][j] = DATE[save]
        elif(i==2):
            calender[i][j] = DATE[save]
            if(j == 28):
                break

        else:
            calender[i][j] = DATE[save]
            if(j == 30):
                break
# print(calender)
print(calender[x][y])