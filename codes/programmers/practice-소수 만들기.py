nums1 = [1,2,3,4]  # 1
nums2 = [1,2,7,6,4]  # 4



def check(num):

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1



def solution(nums):
    
    from itertools import combinations
    tmp = []
    tmp.extend(list(combinations(nums, 3)))

    answer = 0
    for t in tmp:
        answer += check(sum(t))

    return answer



print(solution(nums1))
print(solution(nums2))