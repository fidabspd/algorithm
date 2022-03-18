n, k = map(int, input().split(' '))


def to_binary(n):
    b = []
    one_idx = []
    i = 0
    while n:
        a, n = n%2, n//2
        b = [a]+b
        if a == 1:
            one_idx.append(i)
        i += 1
        
    one_idx = sorted(list(map(lambda x: -x+len(b)-1, one_idx)))
    return b, one_idx

def to_decimal(b):
    mul = 1
    d = 0
    for i in b[::-1]:
        d += i*mul
        mul *= 2
    return d

def solution(n, k):
    b, one_idx = to_binary(n)
    if len(one_idx) <= k:
        return 0
    answer_b = [-i+1 for i in b[one_idx[k-1]+1:one_idx[-1]]] + \
               [1] + [0]*(len(b)-one_idx[-1]-1)
    answer = to_decimal(answer_b)
    return answer


print(solution(n, k))
