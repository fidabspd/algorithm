n = 6; vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


### 시간 초과
def solution1(n, vertex):
    
    dists = [0]*n
    
    vertex.sort()
    for v in vertex:
        if v[0] > v[1]:
            v[0], v[1] = v[1], v[0]
    
    for destination in range(2, n+1):
        now = [1]
        dist = 1
        fastbreak = False  # 2중 for문 break용
        while dists[destination-1] == 0:  # 거리 찾기 전까지 계속
            tmp = []  # tmp 초기화

            for v in vertex:
                for n in now:
                    if v[0] == n:
                        if v[1] != destination:  # 중간 경유지일 경우
                            if v[1] not in tmp:
                                tmp.append(v[1])

                        else:  # 목적지 찾았으면 2중 for문 break
                            dists[destination-1] = dist
                            fastbreak = True
                            break        
                if fastbreak == True:
                    break

            dist += 1
            now = tmp
    
    return dists.count(max(dists))


### 틀림
def solution2(n, vertex):

    dists = [0] * n  # 1로부터의 거리
    now = [1]  # 현위치 노드
    tmp = []  # 현 위치와 이어져있는 노드
    dist = 1  # tmp와 1노드 사이 거리

    while dists.count(0) != 1:  # 1번 노드를 제외한 나머지 노드들의 거리를 다 찾을때 까지
        for v in vertex:
            for n in now:
                if n in v:  # now가 vertex안에 들어있다면
                    if v[v.index(n)-1] not in tmp and dists[v[v.index(n)-1]-1] == 0:
                        tmp.append(v[v.index(n)-1])  # 이어진 노드 tmp에 추가

            for t in tmp:
                if dists[t-1] == 0 and t != 1:  # 해당 node의 dist가 비어있다면 할당
                    dists[t-1] = dist

        print(f'dist: {dist-1}, dists: {dists}, now: {now}, tmp: {tmp}')

        now = tmp
        dist += 1

    return dists.count(max(dists))


### 시간 초과
def solution3(n, vertex):

    dists = [0] * n  # 1로부터의 거리
    now = [1]  # 현위치 노드
    dist = 1  # tmp와 1노드 사이 거리

    while dists.count(0) != 1:  # 1번 노드를 제외한 나머지 노드들의 거리를 다 찾을때 까지
        tmp = []  # 현 위치와 이어져있는 노드
        
        for v in vertex:
            for n in now:
                if n in v:  # now가 vertex안에 들어있다면
                    if v[v.index(n)-1] not in tmp and dists[(v[v.index(n)-1])-1] == 0 and v[v.index(n)-1] != 1:
                        tmp.append(v[v.index(n)-1])  # 이어진 노드 tmp에 추가

            for t in tmp:
                if dists[t-1] == 0 and t != 1:  # 해당 node의 dist가 비어있다면 할당
                    dists[t-1] = dist

        print(f'dist: {dist-1}, dists: {dists}, now: {now}, tmp: {tmp}')

        now = tmp
        dist += 1

    return dists.count(max(dists))


print(solution3(n, vertex))