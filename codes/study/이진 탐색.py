### 떡 자르기

n, m = list(map(int, input().split(' ')))
lengths = list(map(int, input().split(' ')))


def solution(m, lengths):
    start = 0
    end = max(lengths)
    answer = 0
    
    while start <= end:
        mid = (start+end)//2
        total = sum([max(0, i-mid) for i in lengths])
        if total < m:
            end = mid-1
        else:
            start = mid+1
            answer = mid
            
    return answer


print(solution(m, lengths))




### 특정 수 개수 구하기

n, x = list(map(int, input().split(' ')))
lst = list(map(int, input().split(' ')))


def solution(x, lst):
    import bisect
    return bisect.bisect_right(lst, x) - bisect.bisect_left(lst, x)


print(solution(x, lst))
