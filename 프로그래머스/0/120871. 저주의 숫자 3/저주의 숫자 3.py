def solution(n):
    n_list = []
    index = 0
    num = 1
    while index < 100:
        if num % 3 != 0 and "3" not in str(num):
            n_list.append(num)
            index += 1
        num += 1    
    return n_list[n - 1]