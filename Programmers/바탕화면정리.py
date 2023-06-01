def solution(wallpaper):
    # answer = [51, 51, 0, 0]
    # lux, luy, rdx, rdy= 0, 1, 2, 3
    
    # for i, elements in enumerate(wallpaper):
    #     print(i,elements)
    #     for j, element in enumerate(elements):
    #         if element == '#':
    #             answer[lux] = min(answer[lux], i)
    #             answer[luy] = min(answer[luy], j)
    #             answer[rdx] = max(answer[rdx], i+1)
    #             answer[rdy] = max(answer[rdy], j+1)
                
    # return answer
    answer = []
    min_location_y = 60
    min_location_x = 60
    max_location_y = 0
    max_location_x = 0
    for i, paper in enumerate(wallpaper):
        for j, p in enumerate(paper):
            if(p == '#'):
                    if(i<min_location_y):
                        min_location_y = i
                    if( j<min_location_x):
                        min_location_x = j
                        
                    if(i+1 > max_location_y):
                        max_location_y = i+1
                    if( j+1 > max_location_x):
                        max_location_x = j+1
    answer.append([min_location_y,min_location_x,max_location_y,max_location_x])
    
    return answer


wallpaper = []
wallpaper.append([".#...", "..#..", "...#."])
wallpaper.append(["..........", ".....#....", "......##..", "...##.....", "....#....."])
wallpaper.append([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
wallpaper.append(["..", "#."])
print(solution(wallpaper))