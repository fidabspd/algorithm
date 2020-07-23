n1 = 3; computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]  # 2
n2 = 3; computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]  # 1
n3 = 5; computers3 = [[1, 0, 1, 0, 0], [0, 1, 1 ,0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]  # 2
n4 = 5; computers4 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1]]  # 3
n4 = 3; computers5 = [[1,1,0], [1,1,1], [0,1,1]]  # 1

def solution(n, computers):

    answer = 0
    now = 0

    while computers:  # computer가 빌때까지
        for com in computers:
            com.pop(now)  # now의 col을 다 지움
            
        try:
            tmp = computers[now].index(1)  # tmp = 다음번 now
        except:  # now의 row에 1이 없으면 (더이상 이어지는 컴퓨터가 없으면)
            answer += 1  # 네트워크 += 1
            tmp = 0  # 다음번 now가 될 tmp 초기화
        computers.pop(now)  # tmp를 빼내고 나서 now의 row pop
        
        
        
        print(f'now: {now}, tmp: {tmp}')
        print(f'answer: {answer}')
        for com in computers:
            print(com)
        print('\n', end = '')
        
        
        
        now = tmp  # now 업데이트
        
    return answer

# print(solution(n1, computers1))
# print(solution(n2, computers2))
# print(solution(n3, computers3))
print(solution(n4, computers4))