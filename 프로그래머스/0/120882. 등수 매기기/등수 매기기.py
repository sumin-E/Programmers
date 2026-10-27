def solution(score):
    answer = []
    for i in score:
        answer.append(i[0] + i[1])
    for x in range(len(answer)):
        count = 1
        for y in range(len(answer)):
            if answer[x] < answer[y]:
                count += 1
        score[x] = count
    return score