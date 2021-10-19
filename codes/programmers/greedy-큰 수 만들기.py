number1 = "1924"; k1 = 2  # "94"
number2 = "1231234"; k2 = 3  # "3234"
number3 = "4177252841"; k3 = 4  # "775841"


### 시간초과
def solution(number, k):
    number_list = list(number)
    
    for idx, num in enumerate(number):
        for comp in number[idx+1:idx+1+k]:
            if num < comp:
                number_list.remove(num)
                k -= 1
                break
        if k == 0:
            break
            
    if k != 0:
        number_list = number_list[:-k]
        
    return ''.join(number_list)
            
print(solution(number1, k1))
print(solution(number2, k2))
print(solution(number3, k3))
print(solution('987654321', 3))







### 틀림(왜틀린지는 모르겠다), 시간초과
def solution(number, k):
    _k = k
    idx = 0
    answer = list(number)  # 삭제하고 내보낼 것
    number_list = list(number)  # 그대로 두고 iter 돌 것
    
    while idx + k < len(number_list):
        num = number_list[idx]
        print(f'number: {num}')
        
        tmp = 0  # 뒤로 몇번째 comp가 num보다 큰지
        for comp in number_list[idx+1:idx+1+k]:  # num의 다음 숫자부터 k개 만큼 iter 돌기
            tmp += 1  # num 뒤로 몇번째 comp가 num보다 큰지
            if num < comp:
                for _ in range(tmp):  # num보다 큰 comp가 나오기 전 앞부분 전부 삭제
                    #print(f'k = {k}, {answer}의 {idx - _k + k}번째 요소인 {answer[idx - _k + k]} 지움\n')
                    answer.pop(idx - _k + k)
                idx += tmp
                k -= tmp
                break
        else:
            #print(f'{answer, answer[idx - _k + k]}삭제하지 않음\n')
            idx += 1
            
        if k == 0:
            return answer
            break
    
    return answer[:-k]
            
print(solution(number1, k1), '\n\n\n')
print(solution(number2, k2), '\n\n\n')
print(solution(number3, k3), '\n\n\n')
print(solution('987654321', 3), '\n\n\n')
print(solution('123456', 2), '\n\n\n')






### 통과
from collections import deque
def solution(number, k):  # number에서 que형태로 answer에 스택
    answer = deque([])
    number = deque(number)
    num = number.popleft(); comp = number.popleft()
    
    while k > 0:  # k가 남아있는 동안
        #print(f'answer: {answer}, num: {num}, comp: {comp}, number: {number}')
        if num < comp:  # answer의 가장 오른쪽이 number의 가장 왼쪽보다 작으면 
            if not answer:  # answer가 비어있으면
                num = comp  # comp를 num으로
                comp = number.popleft()
            else:
                num = answer.pop()  # answer의 그 다음으로 num 업데이트
            k -= 1  # 제거한 만큼 k줄이기
            
        else:  # answer의 가장 오른쪽이 number의 가장 왼쪽보다 크거나 같으면
            answer.append(num)  # answer에 다시 집어넣고
            num = comp  # answer의 가장 오른쪽을 comp로 업데이트
            comp = number.popleft()  # comp다시 꺼내기
            
        if len(number) == k-1:  # number에 뽑을 k가 충분치 않으면
            return ''.join(answer) + max(num, comp)
            
    return ''.join(answer) + num + comp + ''.join(number)
            
    
print(solution(number1, k1), '\n\n\n')
print(solution(number2, k2), '\n\n\n')
print(solution(number3, k3), '\n\n\n')
print(solution('987654321', 3), '\n\n\n')
print(solution('987653421', 3), '\n\n\n')
print(solution('123456', 2), '\n\n\n')



### 다른 사람의 풀이
def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
