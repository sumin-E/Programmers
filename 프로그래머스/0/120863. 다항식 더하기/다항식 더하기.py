def solution(polynomial):
    answer = ()
    a = 0
    b = 0
    s_poly = polynomial.split("+")
    for i in s_poly:
        i = i.replace(" ", "")
        if i[-1] == "x":
            if i == "x":
                a += 1
            else:
                a += int(i[:-1])
        else:
            b += int(i)
    if a != 0 and a != 1 and b != 0:
        answer = str(a) + "x" + " + " + str(b)
    elif a == 1 and b != 0:
        answer = "x" + " + " + str(b)
    elif a != 0 and a != 1 and a != 1:
        answer = str(a) + "x"
    elif a == 1:
        answer = "x"
    elif b != 0:
        answer = str(b)
        
    return answer