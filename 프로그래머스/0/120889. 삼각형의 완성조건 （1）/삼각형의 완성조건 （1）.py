def solution(sides):
    answer = 0
    big = max(sides)
    sides.remove(big)
    answer = 1 if sum(sides) > big else 2
    return answer