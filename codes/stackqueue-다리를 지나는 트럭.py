bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# return 8

### 테스트5 시간 초과
def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights
    trk_now = [0] * bridge_length  # 다리위에 있는 트럭
    
    time = 0
    while True:
        time += 1
        trk_now = trk_now[1:]
        weight_now = sum(trk_now)  # 다리위 트럭 무게 합
        if truck_weights[0] <= weight - weight_now:
            trk_now.append(truck_weights[0])
            truck_weights.remove(truck_weights[0])
            truck_weights.append(0)
        else:
            trk_now.append(0)
        if sum(trk_now) == 0:
            break
        #print(time, trk_now) ####
    
    return time


### 통과
def solution(bridge_length, weight, truck_weights):
    trk_tbl = [[truck_weights[0]], [1]]  # 올라간 트럭의 무게와 경과시간을 해쉬로 표시 (먼저하나태움)
    truck_weights.remove(truck_weights[0])  # 태운트럭은 삭제
    time = 1
    # print(time, trk_tbl)
    while True:
        time += 1  # 시간 경과
        trk_tbl[1] = list(map(lambda x: x + 1, trk_tbl[1]))  # 트럭 경과시간 1 다 더함
        if trk_tbl[1][0] > bridge_length:  # 트럭이 빠져나갈때가 되면 나가게 함
            trk_tbl[0] = trk_tbl[0][1:]
            trk_tbl[1] = trk_tbl[1][1:]
        weight_now = sum(trk_tbl[0])  # 트럭 무게 총 합
        if len(truck_weights) != 0 and truck_weights[0] <= weight - weight_now:  # 남은 트럭이 있고, 트럭이 탈수있으면 태움
            trk_tbl[0].append(truck_weights[0])
            trk_tbl[1].append(1)
            truck_weights.remove(truck_weights[0])
        if len(trk_tbl[0]) == 0:  # 다리 위 트럭 무게가 0이면 멈춤
            # print(time)
            break
    return time
        # print(time, trk_tbl)


### 약간 더 빠른가..?
def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights
    trk_tbl = [[truck_weights[0]], [1]]  # 올라간 트럭의 무게와 경과시간을 해쉬로 표시 (먼저하나태움)
    weight_now = truck_weights[0]
    truck_weights.remove(truck_weights[0])  # 태운트럭은 삭제
    time = 1  # 시작시간 1
    # print(time, trk_tbl)
    while True:
        time += 1  # 시간 경과(루프 들어오면 바로 2부터 - 다리길이가 1이상이므로 괜찮음)
        trk_tbl[1] = list(map(lambda x: x + 1, trk_tbl[1]))  # 트럭 경과시간 1 다 더함
        if trk_tbl[1][0] > bridge_length:  # 트럭이 빠져나갈때가 되면 나가게 함
            weight_now -= trk_tbl[0][0]
            trk_tbl[0] = trk_tbl[0][1:]
            trk_tbl[1] = trk_tbl[1][1:]
        if len(truck_weights) != 0 and truck_weights[0] <= weight - weight_now:  # 남은 트럭이 있고, 트럭이 탈수있으면 태움
            weight_now += truck_weights[0]
            trk_tbl[0].append(truck_weights[0])
            trk_tbl[1].append(1)
            truck_weights.remove(truck_weights[0])
        if len(trk_tbl[0]) == 0:  # 다리 위 트럭 무게가 0이면 멈춤
            # print(time)
            break
        # print(time, trk_tbl, weight_now)
    return time


print(solution(bridge_length, weight, truck_weights))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))