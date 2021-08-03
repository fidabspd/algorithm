s1 = "3people unFollowed me"  # "3people Unfollowed Me"
s2 = "for the last week"  # "For The Last Week"


def solution(s):
    answer = ''
    is_upper = True
    for str_ in s:
        if is_upper:
            answer += str_.upper()
        else:
            answer += str_.lower()
        if str_ == ' ':
            is_upper = True
        else:
            is_upper = False
    return answer


print(solution(s1))
print(solution(s2))
