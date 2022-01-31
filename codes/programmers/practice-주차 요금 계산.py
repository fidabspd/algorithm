fees1 = [180, 5000, 10, 600]
records1 = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN", 
    "23:00 5961 OUT"
]  # [14600, 34400, 5000]
fees2 = [120, 0, 60, 591]
records2 = [
    "16:00 3961 IN",
    "16:00 0202 IN",
    "18:00 3961 OUT",
    "18:00 0202 OUT",
    "23:58 3961 IN"
]  # [0, 591]
fees3 = [1, 461, 1, 10]
records3 = ["00:00 1234 IN"]  # [14841]


def solution(fees, records):
    from collections import deque
    base_time, base_rate, unit_time, unit_rate = fees
    ins = {}
    res = {}
    for record in records:
        t, n, s = record.split(' ')
        h, m = t.split(':')
        t = int(h)*60 + int(m)
        if s == 'IN':
            ins[n] = t
        else:
            if n in res.keys():
                res[n] += t-ins[n]
            else:
                res[n] = t-ins[n]
            ins[n] = None
    print(res)
    print(ins)


print(solution(fees1, records1))
print(solution(fees2, records2))
print(solution(fees3, records3))
