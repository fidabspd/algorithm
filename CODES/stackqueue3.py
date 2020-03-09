progresses = [93,30,55]
speeds = [1,30,5]
# return = [2,1]

### 통과
def solution(progresses, speeds):
    progresses = progresses
    speeds = speeds
    time = 0
    answer = []
    while True:
        # print(progresses, speeds)
        for step in range(len(progresses)):  # 하루 경과
            progresses[step] += speeds[step]
        

        len_now = len(progresses)
        tmp = 0
        for step in range(len(progresses)):  # 배포
            if progresses[0] >= 100:  # 첫번째가 100이 넘는지 확인
                tmp += 1
                progresses.remove(progresses[0])
                speeds.remove(speeds[0])
            else:  # 아니면 break
                break
        if len_now != len(progresses):  # 배포된게 하나라도 있으면 
            answer.append(tmp)
        if len(progresses) == 0:
            break
    return answer

# print(solution(progresses, speeds))


### 프로그래머스 다른 풀이
#   작업을 진행하지 않고 작업일수만 계산함.
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0] < -((p-100)//s):
            # -((p-100)//s)는 남은 작업일수 ***100-p을 쓰게 되면 올림을 해야함.
            # 바로 앞 작업의 남은 작업일수보다 뒷작업의 작업일수가 더 크면 따로 배포
            Q.append([-((p-100)//s),1])
            # 남은 작업일수, 배포 개수 append
        else:
            Q[-1][1]+=1
            # 아니면 같이 배포하고 배포개수 1추가
        print(Q)
    return [q[1] for q in Q]  # 배포되는 개수 들만 list로 출력

print(solution(progresses, speeds))