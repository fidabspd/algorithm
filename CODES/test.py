numbers1 = [6, 10, 2]  # return "6210"
numbers = [3, 30, 34, 5, 9]  # return "9534330"

#a = sorted(numbers, key = lambda x: str(x) + str(x)[-1] * (len(str(numbers[-1])) - len(str(x))), reverse = True)
#print(list(map(lambda x: str(x) + str(x)[-1] * (len(str(numbers[-1])) - len(str(x))), numbers)))
#print(a)

#a = lambda x: str(x) + str(x)[-1] * (len(str(numbers[-1])) - len(str(x)))
#print(a(1))

a = lambda x: str(x) + str(x)[0] * (len(str(max(numbers))) - len(str(x)))
print(sorted(list(map(a, numbers)), reverse=True))