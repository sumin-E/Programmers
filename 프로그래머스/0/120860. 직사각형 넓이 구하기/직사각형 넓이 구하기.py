def solution(dots):
    a = 0
    b = 0
    for i in range(len(dots) - 1):
        if dots[0][0] != dots[1+i][0] and dots[0][1] != dots[1+i][1]:
            a = dots[i+1][0]
            b = dots[i+1][1]

    x = abs(a - dots[0][0])
    y = abs(b - dots[0][1])
    return x * y