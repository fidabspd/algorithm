s1 = "aabbaccc"  # 7
s2 = "ababcdcdababcdcd"  # 9
s3 = "abcabcdede"  # 8
s4 = "abcabcabcabcdededededede"  # 14
s5 = "xababcdcdababcdcd"  # 17


def solution(s):

    answer = len(s)

    for interval in range(1, (len(s)//2)+1):
        s_tmp = s
        answer_tmp = len(s)

        while s_tmp:
            now = s_tmp[:interval]
            s_tmp = s_tmp[interval:]
            count = 1
            while now == s_tmp[:interval]:
                s_tmp = s_tmp[interval:]
                count += 1
            if count > 1:
                answer_tmp = answer_tmp - (count-1)*interval + len(str(count))

        if answer_tmp < answer:
            answer = answer_tmp
    
    return answer


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
