# def solution(numbers):
#     answer = 0
#     return answer

numbers = "17"  # return 3 (7, 17, 71)
numbers1 = "011"  # return 2 (11, 101)

not_ans = int('0' in numbers) + int('1' in numbers)
print(not_ans)

gen = list(set([1, 10, 11, 110, 101]))  # 만들어낸 숫자들에서 중복 제거
not_ans = gen.count(0) + gen.count(1)  # 숫자들 중 0, 1은 미리 not_ans에 추가

for num in gen:
    print('!', num)
    if num not in [0, 1, 2]:
        for i in range(2, num):
            if num % i == 0:
                not_ans += 1
                break

answer = len(gen) - not_ans
print(answer, not_ans)
