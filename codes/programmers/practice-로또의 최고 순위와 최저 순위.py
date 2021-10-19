lottos1 = [44, 1, 0, 0, 31, 25]; win_nums1 = [31, 10, 45, 1, 6, 19]
lottos2 = [0, 0, 0, 0, 0, 0]; win_nums2 = [38, 19, 20, 40, 15, 25]
lottos3 = [45, 4, 35, 20, 3, 9]; win_nums3 = [20, 9, 3, 45, 4, 35]
lottos4 = [1, 2, 5, 6, 7, 8]; win_nums4 = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    same = 0; zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
        if i in win_nums:
            same += 1
            continue
    return [7-same-zero if same+zero>0 else 6, 7-same if same>0 else 6]

print(solution(lottos1, win_nums1))
print(solution(lottos2, win_nums2))
print(solution(lottos3, win_nums3))
print(solution(lottos4, win_nums4))

def solution_else(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
