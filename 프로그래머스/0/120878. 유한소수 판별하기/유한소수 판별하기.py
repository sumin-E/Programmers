def solution(a, b):
    answer = 1
    while b != 1:
        if b % 2 == 0 and a % 2 == 0:
            b //= 2
            a //= 2
        elif b % 5 == 0 and a % 5 == 0:
            b //= 5
            a //= 5
        elif b % 2 == 0 and a % 2 != 0:
            b //= 2
        elif b % 5 == 0 and a % 5 != 0:
            b //= 5
        elif b % a == 0 and a != 1:
            b //= a
            a //= a
        elif a % b == 0 and b != 1:
            a //= b
            b //= b
        else:
            break
    if b > 1:
        answer = 2

    return answer