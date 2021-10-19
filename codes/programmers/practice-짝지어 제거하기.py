s1 = 'baabaa'  # 1
s2 = 'cdcd'  # 0


### 시간 초과
def solution1(s):
    
    i = 0
    length = len(s)
    while i < length-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            length -= 2
            i = i-1 if i-1 > 0 else 0
            continue
        i += 1

    return 1 if len(s)==0 else 0


def solution(s):
    if len(s) < 2 or len(s)%2 == 1:
        return 0
    from collections import deque
    sbf = deque([])
    saf = deque(s)
    before = saf.popleft()
    after = saf.popleft()

    i = 0; length = len(s)
    while i < length-1:
        
        if before == after:
            if len(sbf) == 0:
                if len(saf) == 0:
                    return 1
                elif len(saf) == 1:
                    return 0
                else:
                    before = saf.popleft()
            else:
                before = sbf.pop()
            after = saf.popleft()
            length -= 2
            i = 0 if i == 0 else i-1
        else:
            sbf.append(before)
            before = after
            if len(saf) == 0:
                return 0
            else:
                after = saf.popleft()
            i += 1

    return 1 if len(sbf)==0 else 0


print(solution(s1))
print(solution(s2))


### 다른 사람의 풀이
def solution_else(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return 1 if not(answer) else 0
