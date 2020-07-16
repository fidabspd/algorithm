# 틀림
#def solution(n):
#    answer = 0
#    for num in range(2, n+1):
#        if num % 2 == 0:
#            continue
#        for div in range(2, int(num / 2) + 2):
#            if num % div == 0:
#                break
#        answer += 1

#    return answer

#n = 10
#print(solution(n))



# 제대로 풀이
def solution(n):
    TF = [False, False] + [True] * (n - 1)  # 0, 1은 무조건 False, 2부터는 일단은 True로 놓고 시작
    result = []

    for i in range(n+1):
        if TF[i]:  # i가 소수이면
            result.append(i)
            for j in range(i*2, n+1, i):
                TF[j] = False  # i*2부터 시작해서 i의 배수들은 소수가 아님.
    
    return len(result)

n = 11
print(solution(n))



# 다른 사람의 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)