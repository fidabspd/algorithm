dartResult1 = '1S2D*3T'  # 37
dartResult2 = '1D2S#10S'  # 9
dartResult3 = '1D2S0T'  # 3
dartResult4 = '1S*2T*3S'  # 23
dartResult5 = '1D#2S*3S'  # 51
dartResult6 = '1T2D3D#'  # -4
dartResult7 = '1D2S3T*'  # 59


import re
def solution(dartResult):
    scores = []
    for i in range(3):
        bonus = None
        check = re.search('[0-9]+[SDT]+[#*]*', dartResult).span()[1]
        now, dartResult = dartResult[:check], dartResult[check:]

        if now[-1] in ['#', '*']:
            bonus = now[-1]
            now = now[:-1]

        if now[-1] == 'S':
            score = int(now[:-1])
        elif now[-1] == 'D':
            score = int(now[:-1]) ** 2
        elif now[-1] == 'T':
            score = int(now[:-1]) ** 3

        if bonus == '*':
            score = score * 2
            if i != 0:
                scores[-1] = scores[-1] * 2
        elif bonus == '#':
            score = score * (-1)

        scores.append(score)

    return sum(scores)


print(solution(dartResult1))
print(solution(dartResult2))
print(solution(dartResult3))
print(solution(dartResult4))
print(solution(dartResult5))
print(solution(dartResult6))
print(solution(dartResult7))


def solution_else(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
