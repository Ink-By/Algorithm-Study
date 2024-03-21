def find_numbers(a, b):
    counts = [0] * 10  # 숫자의 등장 횟수를 저장하는 배열

    # 주어진 문장에서 숫자의 등장 횟수를 세는 함수
    def count_occurrences(sentence):
        for digit in sentence:
            counts[int(digit)] += 1

    # 문장에서 각 숫자의 등장 횟수를 계산
    for i in range(a, b + 1):
        sentence = str(i)
        count_occurrences(sentence)

    # 조건을 만족하는 숫자들을 찾아서 출력
    result = []
    for i in range(a, b + 1):
        sentence = str(i)
        valid = all(counts[int(digit)] == int(sentence.count(digit)) for digit in sentence)
        if valid:
            result.append(i)

    return result if result else -1

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
result = find_numbers(a, b)
if result == -1:
    print(-1)
else:
    print(*result)
