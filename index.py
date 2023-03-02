array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
print(len(commands))
for i in range(len(commands)):
    s = array[commands[i][0]-1:commands[i][1]]
    s.sort()
    answer.append(s[commands[i][2]-1])
print(answer)
