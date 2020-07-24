n1 = 3; computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]  # 2
n2 = 3; computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]  # 1
n3 = 5; computers3 = [[1, 0, 1, 0, 0], [0, 1, 1 ,0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]  # 2
n4 = 5; computers4 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1]]  # 3
n5 = 3; computers5 = [[1,1,0], [1,1,1], [0,1,1]]  # 1
n6 = 6; computers6 = [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1]]  # 3


### 틀림
def solution1(n, computers):

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



### 통과
def solution(n, computers):
    answer = 0  # 네트워크 총 개수

    while computers:
        now = 0  # 현재 검사할 com
        check = []  # node의 끝까지 본것
        network = []  # 현 network에 포함된 com

        print(f'computers:')
        for com in computers:
            print(com)
        
        while check != network or not check:  # 현 network에 있는 com과 check를 끝낸 com이 같을때까지 (check가 비어있면 check와 network가 같아도 루프 in)
            print(f'now: {now}, network: {network}, check: {check}')
            for idx, com in enumerate(computers[now]):
                if com == 1 and idx not in network:
                    network.append(idx)
            check.append(now)

            for net in network:
                if net not in check:
                    now = net
                    break

        for net in sorted(network, reverse = True):
            computers.pop(net)
            for com in computers:
                com.pop(net)


        
        answer += 1
        
    return answer

print(solution(n1, computers1))
print(solution(n2, computers2))
print(solution(n3, computers3))
print(solution(n4, computers4))
print(solution(n5, computers5))
print(solution(n6, computers6))
