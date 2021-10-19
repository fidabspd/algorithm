def solution(a, b):
    week = ['FRI', 'SAT', 'SUN','MON','TUE','WED','THU']
    for month in range(1, a):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            b += 31
        elif month == 2:
            b += 29
        else:
            b += 30

    answer = week[b%7 - 1]
    return answer

print(solution(1, 1))
print(solution(5, 24))