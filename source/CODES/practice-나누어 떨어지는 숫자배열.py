arr1 = [5, 9, 7, 10]; divisor1 = 5  # [5, 10]
arr2 = [2, 36, 1, 3]; divisor2 = 1 # [1, 2, 3, 36]
arr3 = [3,2,6]; divisor3 = 10  # [-1]

def solution(arr, divisor):
    answer = []
    for val in arr:
        if val%divisor == 0:
            answer.append(val)
    if len(answer) == 0:
        answer = [-1]
    answer.sort()
    return answer

print(solution(arr1, divisor1))
print(solution(arr2, divisor2))
print(solution(arr3, divisor3))

# 다른 사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]