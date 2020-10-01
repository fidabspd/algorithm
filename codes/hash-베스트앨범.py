genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'jazz']
plays = [500, 600, 150, 800, 2500, 2500]

def solution(genres, plays):
    dic_sum = {}
    for gen, ply in zip(genres, plays):
        try:
            dic_sum[gen] += ply
        except:
            dic_sum[gen] = ply
    dic_sum = dict(sorted(dic_sum.items(), reverse = True, key = lambda x: x[1]))

    dt = [[gen, ply, idx] for gen, ply, idx in zip(genres, plays, range(len(genres)))]
    dt = sorted(dt, reverse = True, key = lambda x: x[1])
    dt = sorted(dt, reverse = True, key = lambda x: dic_sum[x[0]])

    dic_total = {}
    for gen, ply, idx in dt:
        try:
            if len(dic_total[gen]) == 2:
                continue
            dic_total[gen].append([ply, idx])
        except:
            dic_total[gen] = [[ply, idx]]

    answer = []
    for ply_idx in dic_total.values():
        for ply, idx in ply_idx:
            answer.append(idx)

    print(dic_sum)
    print(dt)
    print('dic_total:', dic_total)
    return answer

print(solution(genres, plays))



def solution(genres, plays):
    answer = []
    dic = {gen:[] for gen in set(genres)}  # 장르별 딕셔너리 생성
    for gen, ply, le in zip(genres, plays, range(len(plays))):
        dic[gen].append([ply , le])  # dict의 value로 있는 빈 리스트에 하나씩 [ply, le] 값 추가
    genreSort =sorted(list(dic.keys()), key = lambda x: sum(map(lambda y: y[0], dic[x])), reverse = True)
    # sum(map(lambda y: y[0], dic[x])) -> dic 딕셔너리에서 ply만 뽑아내서 같은 gen끼리 합
    for gen in genreSort:
        temp = [e[1] for e in sorted(dic[gen], key = lambda x: (-x[0], x[1]))]
        # 각 장르별로 roop돌면서 index만을 뽑아냄 정렬 순서는 오름차순으로 -ply, index
        answer += temp[:min(len(temp),2)]
        # min(len(temp),2) -> len(temp)와 2중 최소값만을 리턴
        # temp[:min(len(temp),2)] -> temp에서 위에서 뽑은 값의 index까지만 순차적으로 리턴
        # 이후 해당 리스트를 answer에 extend
    return answer

print(solution(genres, plays))

