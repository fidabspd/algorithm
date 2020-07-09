par1 = ['leo', 'kiki', 'eden', 'leo']
com1 = ['leo', 'kiki', 'eden']

# Time complexity N^2
def solution1(participant, completion):
    for person in completion:
        participant.remove(person)
    answer = participant[0]
    return answer

print(solution1(par1, com1))


par1 = ['leo', 'kiki', 'eden', 'leo']
com1 = ['leo', 'kiki', 'eden']

# Time complextity N
def solution2(participant, completion):
    temp = 0
    dic = {}
    for i in participant:
        dic[hash(i)] = i
        temp += hash(i)
    for j in completion:
        temp -= hash(j)
    answer = dic[temp]
    return answer

print(solution2(par1, com1))


par1 = ['leo', 'kiki', 'eden', 'leo']
com1 = ['leo', 'kiki', 'eden']
 
# 프로그래머스 다른사람 풀이
import collections

def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution3(par1, com1))