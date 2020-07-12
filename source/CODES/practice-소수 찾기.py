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

#n = 10
#a = [i for i in range(3, n+1, 2)]
#print(a)

#n = 10

#a = [i for i in range(3, n+1, 2)]
#for i in range(3, n+1 ,2):
#    if i in a :
#        a set([i for i in range(i*2, n+1, i)])

#print(len(a) + 1)

n = 10
a = [False, False] + [True] * (n - 1)
primes = []

print(a)

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(i * 2, n + 1, i):
            print(j)
            a[j] = False
print(primes)