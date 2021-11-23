word1 = "AAAAE"  # 6
word2 = "AAAE"  # 10
word3 = "I"  # 1563
word4 = "EIO"  # 1189


def next_word(word):
    if len(word) != 5:
        word += ' '*(5-len(word))
    word_num_dict = {' ': 0, 'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    num = []
    for w in word:
        num.append(word_num_dict[w])

    for i in range(4, 0, -1):
        if num[i] == 0 and num[i-1] == 0:
            continue
        else:
            num[i] += 1
            break

    for i in range(4, 0, -1):
        if num[i] == 6:
            num[i] = 0
            num[i-1] += 1
        else:
            break

    num_word_dict = {0: '', 1: 'A', 2: 'E', 3: 'I', 4: 'O', 5: 'U'}
    new_word = ''
    for n in num:
        new_word += num_word_dict[n]

    return new_word

def solution(word):
    answer = 1
    new_word = 'A'

    while new_word != word:
        new_word = next_word(new_word)
        answer += 1

    return answer


print(solution(word1))
print(solution(word2))
print(solution(word3))
print(solution(word4))


def solution_else(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer
