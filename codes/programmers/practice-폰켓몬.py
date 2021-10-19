nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]

def solution(nums):
    return min(len(set(nums)), len(nums)//2)

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))