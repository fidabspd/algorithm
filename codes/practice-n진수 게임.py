n1 = 2; t1 = 4; m1 = 2; p1 = 1  # 0111
n2 = 16; t2 = 16; m2 = 2; p2 = 1  # 02468ACE11111111
n3 = 16; t3 = 16; m3 = 2; p3 = 2  # 13579BDF01234567



def convert(num, n):
    T = "0123456789ABCDEF"
    q, r = divmod(num, n)
    if q == 0:
        return T[r]
    else:
        return convert(q, n) + T[r]

def solution(n, t, m, p):

    num = 0
    tmp = ''
    while True:
        tmp += convert(num, n)
        if len(tmp) >= t*m:
            break
        num += 1 
    tmp = tmp[:t*m]
    # print(tmp)

    result = ''
    for i in range(p-1, len(tmp), m):
        result += tmp[i]

    return result



print(solution(n1, t1, m1, p1))
print(solution(n2, t2, m2, p2))
print(solution(n3, t3, m3, p3))