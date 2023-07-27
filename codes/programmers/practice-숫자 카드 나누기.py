# https://school.programmers.co.kr/learn/courses/30/lessons/135807
arrayA0 = [10, 17]
arrayB0 = [5, 20]  # 0
arrayA1 = [10, 20]
arrayB1 = [5, 17]  # 10
arrayA2 = [14, 35, 119]
arrayB2 = [18, 30, 102]  # 7


def solution(arrayA, arrayB):
    def get_div(n):
        div = []
        for i in range(1, int((n**0.5)) + 1):
            if n % i == 0:
                div.append(i)
                div.append(n // i)
        return sorted(div, reverse=True)

    def check_if_div(array, n):
        for i in array:
            if i % n != 0:
                return False
        return True

    def check_if_not_div(array, n):
        for i in array:
            if i % n == 0:
                return False
        return True

    answer = 0
    arrayA.sort()
    arrayB.sort()
    for i in get_div(arrayA[0]):
        if check_if_div(arrayA, i) and check_if_not_div(arrayB, i):
            answer = i
            break
    for j in get_div(arrayB[0]):
        if j < answer:
            break
        if check_if_not_div(arrayA, j) and check_if_div(arrayB, j):
            if answer < j:
                answer = j
    return answer


print(solution(arrayA0, arrayB0))
print(solution(arrayA1, arrayB1))
print(solution(arrayA2, arrayB2))
