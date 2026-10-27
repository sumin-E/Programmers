def solution(id_pw, db):
    answer = ""
    iid = id_pw[0]
    pw = id_pw[1]
    for i in db:
        if i[0] != iid:
            answer = "fail"
        elif i[0] == iid and i[1] != pw:
            answer = "wrong pw"
            break
        else:
            answer = "login"
            break
    return answer