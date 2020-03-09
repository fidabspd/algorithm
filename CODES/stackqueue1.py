heights = [6,9,5,7,4]
ans = [0,0,2,2,4]

def solution(heights):
    answer = []
    for i in range(len(heights)):
        tmp = heights[:i+1]
        for j in range(len(tmp) - 1, -1,-1):
            if tmp[j] > heights[i]:
                answer.append(j + 1)
                break
        if len(answer) <= i:
            answer.append(0)
    return answer

print(solution(heights))



# 프로그래머스 다른 풀이
def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans

print(solution(heights))