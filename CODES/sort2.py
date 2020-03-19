numbers1 = [6, 10, 2]  # return "6210"
numbers = [3, 30, 34, 5, 9]  # return "9534330"



### 알고리즘 틀림
def solution1(numbers):
    from functools import reduce
    numbers.sort()
    origin = numbers
    length = len(str(max(numbers)))
    numbers = [str(num) for num in numbers]
    arr = []
    for idx, num in zip(range(len(numbers)), numbers):
        tmp = num + num[-1] * (length - len(num))
        arr.append([origin[idx], tmp])

    ans = sorted(arr, key = lambda x: x[1], reverse = True)
    return reduce(lambda x, y: x + y, [str(num) for num, id in ans])

#print(solution1(numbers))
#print(solution1(numbers1))



### 알고리즘 틀림
def solution(numbers):
    from functools import reduce
    numbers.sort(reverse = True)
    return reduce(lambda x, y : str(x) + str(y), sorted(numbers, key = lambda x: str(x) + str(x)[0] * (len(str(max(numbers))) - len(str(x))), reverse = True))

print(solution(numbers))
print(solution([0,0,0,0]))
print(solution([12,121]))
print(solution([31,313]))