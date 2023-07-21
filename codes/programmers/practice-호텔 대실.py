# https://school.programmers.co.kr/learn/courses/30/lessons/155651
book_time0 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]  # 3
book_time1 = [["09:10", "10:10"], ["10:20", "12:20"]]  # 1
book_time2 = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]  # 3


def solution(book_time):
    import heapq

    def convert_to_minute(time):
        h, m = time.split(":")
        return int(h) * 60 + int(m)

    new_book_time = []
    check_times = []
    for ci, co in book_time:
        ci, co = convert_to_minute(ci), convert_to_minute(co) + 10
        heapq.heappush(check_times, ci)
        heapq.heappush(check_times, co)
        heapq.heappush(new_book_time, [ci, co])

    n_room = 0
    answer = 0
    out_times = []
    while check_times:
        t = heapq.heappop(check_times)
        if out_times and t == out_times[0]:
            heapq.heappop(out_times)
            n_room -= 1
        elif new_book_time and t == new_book_time[0][0]:
            _, co = heapq.heappop(new_book_time)
            heapq.heappush(out_times, co)
            n_room += 1
        else:
            raise Exception

        if n_room > answer:
            answer = n_room

    return answer


print(solution(book_time0))
print(solution(book_time1))
print(solution(book_time2))
