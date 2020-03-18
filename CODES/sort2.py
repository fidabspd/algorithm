numbers1 = [6, 10, 2]  # return "6210"
numbers = [3, 30, 34, 5, 9]  # return "9534330"


#print(sorted(numbers, key = lambda num: str(num)[0], reverse = True))

#from functools import reduce
#origin = numbers
#length = len(str(max(numbers)))
#numbers = [str(num) for num in numbers]
#for idx, num in zip(range(len(numbers)), numbers):
#    tmp = num + '0' * (length - len(num))
#    numbers[idx] = tmp

#numbers1 = sorted(numbers, reverse = True)
#print(numbers)
#print(sorted(origin, key = lambda x: index))

#print(reduce(lambda x, y: x + y, sorted(numbers, reverse = True)))

def solution(numbers):
    from functools import reduce
    numbers.sort()
    origin = numbers
    length = len(str(max(numbers)))
    numbers = [str(num) for num in numbers]
    arr = []
    for idx, num in zip(range(len(numbers)), numbers):
        tmp = num + '0' * (length - len(num))
        arr.append([origin[idx], tmp])

    ans = sorted(arr, key = lambda x: x[1], reverse = True)
    return reduce(lambda x, y: x + y, [str(num) for num, id in ans])

print(solution(numbers))
print(solution(numbers1))