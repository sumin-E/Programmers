def solution(A, B):
    answer = 0   
    for i in range(len(A) - 1):
        if A != B:
            answer += 1
            A = A[-1] + A[0:-1]
            print(A, answer)
            if A == B:
                break
        elif A == B:
            answer = 0
            break
    if A != B:
        answer = -1
        
    return answer