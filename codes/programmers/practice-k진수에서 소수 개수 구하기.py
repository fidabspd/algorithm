n1 = 437674; k1 = 3  # 3
n2 = 110011; k2 = 10  # 2


def convert_n(n, k):
    c = ''
    while n > 0:
        n, i = n//k, n%k
        c = str(i)+c
    return c

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    return sum([is_prime(int(num)) for num in convert_n(n, k).split('0') if num])


print(solution(n1, k1))
print(solution(n2, k2))