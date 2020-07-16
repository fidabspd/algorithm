s1 = "AB"; n1 = 1  # "BC"
s2 = "z"; n2 = 1 # "a"
s3 = "a B z"; n3 = 4  # "e F d"

def solution(s, n):
    answer = ''
    for ch in s:
        tmp = ord(ch) + n
        if 97 <= ord(ch) <= 122 and tmp > 122:
            tmp -= 26
        elif 65 <= ord(ch) <= 90 and tmp > 90:
            tmp -= 26
        
        if ch == ' ':
            tmp = ord(ch)
        
        answer += chr(tmp)
    return answer

print(solution(s1, n1))
print(solution(s2, n2))
print(solution(s3, n3))