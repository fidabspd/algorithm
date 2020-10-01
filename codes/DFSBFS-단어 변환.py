begin1 = 'hit'; target1 = 'cog'; words1 = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']  # 4
begin2 = 'hit'; target2 = 'cog'; words2 = ['hot', 'dot', 'dog', 'lot', 'log']  # 0

def solution(begin, target, words):
    
    if target not in words:
        return 0

    answer = 0
    now_list = [begin]

    while words:
        next_list = []
        for now in now_list:
            for word in words:
                diff = 0
                for a, b in zip(now, word):
                    if a != b:
                        diff += 1
                if diff == 1:
                    next_list.append(word)

        answer += 1
        if target in next_list:
            return answer

        now_list = next_list

        for next in next_list:
            words.remove(next)
            
print(solution(begin1, target1, words1))
print(solution(begin2, target2, words2))