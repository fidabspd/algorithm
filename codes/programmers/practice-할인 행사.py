want0 = ["banana", "apple", "rice", "pork", "pot"]
number0 = [3, 2, 2, 2, 1]
discount0 = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
# 3
want1 = ["apple"]
number1 = [10]
discount1 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
# 0


def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 9):
        discount_tmp = discount[i:i + 10]
        check = True
        for w, n in zip(want, number):
            if n != discount_tmp.count(w):
                check = False
                break
        if check:
            answer += 1
    return answer


print(solution(want0, number0, discount0))
print(solution(want1, number1, discount1))
