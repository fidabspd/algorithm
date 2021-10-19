n1 = 78  # 83
n2 = 15  # 23

def solution(n):
    ori = n

    # 2진수로 변환
    binary = []
    i = 0
    while True:
        if n < 2**i:
            break
        i += 1
    len_bin = i

    while len(binary) != len_bin:
        i -= 1
        if n < 2**i:
            binary.append(0)
            continue
        n -= 2**i
        binary.append(1)

    if sum(binary) == len_bin:
        return ori + 2**(len_bin-1)

    # 다음 큰 숫자
    tmp = []
    while binary:
        tmp.append(binary.pop())
        if tmp[-2:] == [1, 0]:
            len_tmp = len(tmp)
            break
    else:
        len_tmp = len(tmp) + 1

    binary.extend([1] + [0]*(len_tmp-tmp.count(1)) + [1]*(tmp.count(1)-1))
    binary

    answer = 0
    i = len(binary) - 1
    while binary:
        answer += binary.pop(0) * (2**i)
        i -= 1

    return answer

print(solution(n1))
print(solution(n2))
print(solution(6))


### 다른 사람의 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')  # n의 1 개수 세기
    while True:
        n = n + 1  # n을 1씩 증가시키면서
        if num1 == bin(n).count('1'):  # n의 개수가 같아지면 리턴
            return n

print(nextBigNumber(n1))
print(nextBigNumber(n2))
print(nextBigNumber(6))
