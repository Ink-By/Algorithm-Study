import sys
fruit = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(6)]
big_w = 0
big_w_index = 0
big_h = 0
big_h_index = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if (big_w < arr[i][1]):
            big_w = arr[i][1]
            big_w_index = i
    else:
        if (big_h < arr[i][1]):
            big_h = arr[i][1]
            big_h_index = i
print((big_w_index-1)%6, (big_w_index+1)%6)
print((big_h_index-1)%6, (big_h_index+1)%6)

short_h = abs(arr[(big_w_index-1) % 6][1]-arr[(big_w_index+1) % 6][1])
short_w = abs(arr[(big_h_index-1) % 6][1]-arr[(big_h_index+1) % 6][1])
area = (big_w*big_h)-(short_h*short_w)
print(area*fruit)
