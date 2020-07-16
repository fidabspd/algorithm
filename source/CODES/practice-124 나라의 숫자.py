n1 = 1  # 1
n2 = 2  # 2
n3 = 3  # 4
n4 = 4  # 11
n5 = 5  # 12
n6 = 6  # 14
n7 = 7  # 21
n8 = 8  # 22
n9 = 9  # 24
n10 = 10  # 41

def howlong(num):  # 총 몇자리인지
    tmp = 0; i = 0
    while num > tmp:
        i += 1
        tmp += 3 ** i
    return i

def solution(n):
    length = howlong(n)
    answer = [''] * length
    
    for i in range(length):
        tmp = (n-1) % (3**(i+1)) + 1
        _answer = tmp // (3**i)
        n -= tmp
        
        if _answer == 3:
            _answer = 4
            
        answer[-(i+1)] = str(_answer)
        
    return ''.join(answer)

for i in range(1, 100):
    print(f'i: {i},\t answer: {solution(i)}')




### 다른 사람의 풀이
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


print(change124(10))