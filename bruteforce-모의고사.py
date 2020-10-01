answers = [1,2,3,4,5]  # return [1]
answers1 = [1,3,2,4,2]  # return [1,2,3]

### 통과
def solution(answers):
    cnt = [[1, 0], [2, 0], [3, 0]]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, ans in zip(range(len(answers)), answers):
        if a[idx % len(a)] == ans:
            cnt[0][1] += 1
        if b[idx % len(b)] == ans:
            cnt[1][1] += 1
        if c[idx % len(c)] == ans:
            cnt[2][1] += 1
    cnt.sort(key = lambda x: x[1], reverse = True)
    
    answer = [cnt[0][0]]
    if cnt[0][1] == cnt[1][1]:
        answer.append(cnt[1][0])
        if cnt[1][1] == cnt[2][1]:
            answer.append(cnt[2][0])

    return answer

print(solution(answers))
print(solution(answers1))



### 깔끔하게 (다른풀이 참고)
def solution1(answers):
    cnt = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    pattern = [a, b, c]

    for idx, ans in enumerate(answers):
        for i, p in enumerate(pattern):
            if p[idx % len(p)] == ans:
                cnt[i] += 1
    
    answer = []
    for idx, c in enumerate(cnt):
        if c == max(cnt):
            answer.append(idx + 1)
    
    return answer

print(solution1(answers))
print(solution1(answers1))