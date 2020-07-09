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



from functools import reduce



### 시간복잡도를 O(n)으로 바꿔야함
tmp = []
for i, j in zip(prices, prices[1:]):
    tmp.append(j - i)

print(tmp)
   
    

# time으로 잡아보자
# updn -> 현 time기준 주가가 각 자리 값들 기준 몇의 차이를 가지는지
# diff -> 바로 이전 주가와 현 주가 차이


updn = [0]
diff = 0
for time in range(len(prices)):
    updn.append(0)
    # diff = 



    tmp = prices[time]