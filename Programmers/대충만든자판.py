def solution(keymap, targets):
    alphabet = [-1 for i in range(26)]
    answer = []
    keynum = 1
    for i in keymap:
        cnt = 1
        for j in i:
            askii = ord(j) - 65
            if alphabet[askii] > cnt or alphabet[askii] == -1:
                alphabet[askii] = cnt
            cnt += 1
        keynum += 1
    for i in targets:
        sumtarget = 0
        for j in i:
            if alphabet[ord(j) - 65] != -1:
                sumtarget += alphabet[ord(j) - 65]
            else:
                sumtarget = 0
                break
        if sumtarget == 0:
            sumtarget = -1
        answer.append(sumtarget)

    return answer
