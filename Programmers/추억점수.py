def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score = 0
        for k in i:
            if k in name:
                idx = name.index(k)
                score += yearning[idx]
        answer.append(score)
    return answer
