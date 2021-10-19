s1 = "110010101001"  # [3,8]
s2 = "01110"  # [3,3]
s3 = "1111111"  # [4,1]


def solution(s):
    answer = [0, 0]
    while s != '1':
        before_length = len(s)
        s = len([n for n in s if n == '1'])
        answer[1] += before_length - s
        answer[0] += 1
        s = str(bin(s))[2:]
    return answer
    

print(solution(s1))
print(solution(s2))
print(solution(s3))
