n1 = 3; words1 = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']  # [3,3]
n2 = 5; words2 = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']  # [0,0]
n3 = 2; words3 = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']  # [1,3]



def solution(n, words):

    tmp = [words[0]]

    _break = 1
    for w in words[1:]:
        if tmp[-1][-1] == w[0] and w not in tmp:
            tmp.append(w)
        else:
            break
        _break += 1

    if len(tmp) == len(words):
        return [0, 0]

    return [((_break) % n) + 1, ((_break) // n) + 1]



print(solution(n1, words1))
print(solution(n2, words2))
print(solution(n3, words3))