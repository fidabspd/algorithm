gems1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]  # [3, 7]
gems2 = ["AA", "AB", "AC", "AA", "AC"]  # [1, 3]
gems3 = ["XYZ", "XYZ", "XYZ"]  # [1, 1]
gems4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]  # [1, 5]


# 시간 초과
def solution1(gems):
    min_len = len(gems)
    answer = [0, 0]
    start, end = 0, 0
    n_unique = len(set(gems))
    while end < len(gems):
        if len(set(gems[start:end+1])) != n_unique:
            end += 1
        else:
            if start == end:
                return [1, 1]
            if end-start < min_len:
                min_len = end-start
                answer = [start+1, end+1]
            start += 1
            if len(set(gems[start:end+1])) == n_unique:
                continue
            start -= 1
            end += 1
    return answer


# 시간 초과, 틀림
def solution2(gems):  # unique개수 count방식을 set이 아닌 dict로 변경
    min_len = len(gems)
    answer = [0, 0]
    start, end = 0, 0
    unique_gems = list(set(gems))
    check_dict = {gem: 0 for gem in unique_gems}
    check_dict[gems[0]] = 1
    while end < len(gems):
        if list(check_dict.values()).count(0) != 0:
            end += 1
            check_dict[gems[end]] += 1
        else:
            if start == end:
                return [1, 1]
            if end-start < min_len:
                min_len = end-start
                answer = [start+1, end+1]
            check_dict[gems[start]] -= 1
            if list(check_dict.values()).count(0) == 0:
                start += 1
                continue
            check_dict[gems[start]] += 1
            end += 1
    return answer


def solution(gems):
    from collections import defaultdict
    start, end = 0, -1
    n_gems = len(set(gems))
    min_len = len(gems)
    check_n = defaultdict(lambda: 0)

    while True:
        if not len(check_n) == n_gems:
            end += 1
            check_n[gems[end]] += 1
        else:
            if end-start < min_len:
                min_len = end-start
                answer = [start+1, end+1]
            check_n[gems[start]] -= 1
            start += 1

            if check_n[gems[start-1]] == 0:
                start -= 1
                check_n[gems[start]] += 1
                end += 1
                if end >= len(gems):
                    break
                check_n[gems[end]] += 1
                
    return answer
   

print(solution(gems1))
print(solution(gems2))
print(solution(gems3))
print(solution(gems4))