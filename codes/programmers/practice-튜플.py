s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"  # [2, 1, 3, 4]
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"  # [2, 1, 3, 4]
s3 = "{{20,111},{111}}"  # [111, 20]
s4 = "{{123}}"  # [123]
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"  # [3, 2, 4, 1]


def solution(s):
    answer = []
    s = sorted(map(lambda x: list(map(int, x.split(','))), s[2:-2].split(r'},{')), key=len)
    for numbers in s:
        for number in numbers:
            if number not in answer:
                answer.append(number)
    return answer


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
