s = "try hello world"  # "TrY HeLlO WoRlD"


def solution(s):
    answer = ''
    check = 0
    for st in s:
        if st == ' ':
            check = -1
        if check%2 == 0:
            st = st.upper()
        else:
            st = st.lower()
        answer += st
        check += 1
            
    return answer


print(solution(s))
