n1 = 1; t1 = 1; m1 = 5; timetable1 = \
    ["08:00", "08:01", "08:02", "08:03"]  # "09:00"
n2 = 2; t2 = 10; m2 = 2; timetable2 = \
    ["09:10", "09:09", "08:00"]  # "09:09"
n3 = 2; t3 = 1; m3 = 2; timetable3 = \
    ["09:00", "09:00", "09:00", "09:00"]  # "08:59"
n4 = 1; t4 = 1; m4 = 5; timetable4 = \
    ["00:01", "00:01", "00:01", "00:01", "00:01"]  # "00:00"
n5 = 1; t5 = 1; m5 = 1; timetable5 = \
    ["23:59"]  # "09:00"
n6 = 10; t6 = 60; m6 = 45; timetable6 = \
    ["23:59", "23:59", "23:59", "23:59", "23:59", \
     "23:59", "23:59", "23:59", "23:59", "23:59", \
     "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]  # "18:00"


def time_to_int(s):
    s = s.split(':')
    return int(s[0])*60 + int(s[1])

def solution(n, t, m, timetable):
    break_outer = False
    timetable_int = sorted(list(map(time_to_int, timetable)))
    time_now = 9*60-t
    check_index = 0
    for i in range(n):
        time_now += t
        board_p = 0
        if break_outer:
            break
        while board_p < m and time_now >= timetable_int[check_index+board_p]:
            board_p += 1
            if check_index+board_p == len(timetable):
                break_outer = True
                break
        check_index += board_p
    if board_p == m:
        answer = timetable_int[0 if check_index == 0 else check_index-1]-1
    else:
        answer = 9*60+(n-1)*t
    return f'{answer//60:02}:{answer%60:02}'


print(solution(n1, t1, m1, timetable1))
print(solution(n2, t2, m2, timetable2))
print(solution(n3, t3, m3, timetable3))
print(solution(n4, t4, m4, timetable4))
print(solution(n5, t5, m5, timetable5))
print(solution(n6, t6, m6, timetable6))
