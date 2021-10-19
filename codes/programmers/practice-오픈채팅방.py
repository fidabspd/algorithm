record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

def solution(record):
    record.reverse()
    dic = dict()
    for r in record:
        r = r.split()
        if len(r) == 3 and r[1] not in dic.keys():
            dic[r[1]] = r[2]

    result = []
    record.reverse()
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            result.append(f'{dic[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            result.append(f'{dic[r[1]]}님이 나갔습니다.')
        else:
            continue

    return result

print(solution(record))