prices = [1, 2, 3, 2, 3]
# return [4, 3, 1, 1, 0]


### 시간 초과
def solution(prices):
    answer = []
    for idx1 in range(len(prices)):
        cnt = 1
        # print(prices[idx1])
        # print(prices[idx1 + 1:])
        if idx1 != len(prices) - 1:
            for idx2 in range(len(prices[idx1 + 1:])):
                if prices[idx1] <= prices[idx1 + 1:][idx2] and idx2 != len(prices[idx1 + 1:]) - 1:
                    cnt += 1
                else:
                    break
        else:
            answer.append(0)
            break
        answer.append(cnt)
    return(answer)



### 왜 시간초과인지 모르겠다
prices = [1, 2, 3, 2, 3]  # [4, 3, 1, 1, 0]

def solution(prices):
    answer = []
    
    for idx in range(len(prices)):
        p = prices.pop(0)
        tmp = 0
        for f in prices:
            tmp += 1
            if p > f:
                break
        answer.append(tmp)
        
    return answer

print(solution(prices))



### 통과
def solution(prices):
    from collections import deque
    answer = []
    que = deque(prices)
    
    while que:
        p = que.popleft()
        tmp = 0
        for f in que:
            tmp += 1
            if p > f:
                break
        answer.append(tmp)
        
    return answer