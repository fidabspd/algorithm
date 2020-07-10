arr1 = [1,1,3,3,0,1,1]  # answer1 = [1,3,0,1]
arr2 = [4,4,4,3,3]  # answer2 = [4,3]

def solution(arr):
    answer = [arr.pop(0)]
    for val in arr:
        tmp = val
        if tmp != answer[-1]:
            answer.append(tmp)
    return answer

print(solution(arr1))

# 다른사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue  # 포인트
        a.append(i)
    return a