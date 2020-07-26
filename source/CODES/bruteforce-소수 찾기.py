numbers1 = '17'  # 3
numbers2 = '011'  # 2


### 통과
def solution(numbers):
    from itertools import permutations

    perm = []
    for i in range(1, len(numbers)+1):
        perm.extend(list(map(''.join, permutations(numbers, i))))
    perm = set(map(int, perm))
    print(perm)
    
    answer = 0
    for p in perm:

        if p in [0, 1]:
            continue

        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                break
        else:
            answer += 1

    return answer


### 에라토스테네스의 체 사용
def mklst(limit):
    result = [False]*2 + [True]*(limit-1)
    lst = []
    
    for num in range(limit+1):
        if result[num] == True:
            lst.append(num)
            for no in range(num*2, limit+1, num):
                result[no] = False
                
    return lst

def solution1(numbers):
    from itertools import permutations

    answer = 0
    perm = []
    for i in range(1, len(numbers)+1):
        perm.extend(list(map(''.join, permutations(numbers, i))))
    perm = set(map(int, perm))
    
    lst = mklst(max(perm))
    for p in perm:
        if p in lst:
            answer += 1

    return answer

print(solution(numbers1))
print(solution(numbers2))
