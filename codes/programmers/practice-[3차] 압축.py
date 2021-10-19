msg1 = 'KAKAO'  # [11, 1, 27, 15]
msg2 = 'TOBEORNOTTOBEORTOBEORNOT'  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
msg3 = 'ABABABABABABABAB'  # [1, 2, 27, 29, 28, 31, 30]


def solution(msg):
    answer = []
    index_dict = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 27)))
    new_index = 27

    i = 0
    while True:
        length = 1
        while True:
            check_str = msg[i:i+length]
            if len(check_str) < length:
                answer.append(index_dict[check_str])
                return answer
            if check_str in index_dict.keys():
                length += 1
                continue
            index_dict[check_str] = new_index
            new_index += 1
            answer.append(index_dict[check_str[:-1]])
            i += length-1
            break


print(solution(msg1))
print(solution(msg2))
print(solution(msg3))
