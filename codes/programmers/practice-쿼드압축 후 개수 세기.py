arr1 = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]  # [4,9]
arr2 = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],
        [0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]  # [10,15]


import numpy as np
def solution(arr):
    answer = [0, 0]
    for a in arr:
        answer[0] += a.count(0)
        answer[1] += a.count(1)

    quad_loc = np.array([[0]*len(arr)]*len(arr))
    arr = np.array(arr)
    now_len = len(arr)
    while now_len > 1:
        for i in range(len(arr)//now_len):
            for j in range(len(arr)//now_len):
                i_s, i_e, j_s, j_e = i*now_len, (i+1)*now_len, j*now_len, (j+1)*now_len
                if sum(sum(quad_loc[i_s:i_e, j_s:j_e])) != 0:
                    continue
                arr_tmp = arr[i_s:i_e, j_s:j_e]
                arr_tmp_sum = sum(sum(arr_tmp))
                if arr_tmp_sum == now_len**2:
                    quad_loc[i_s:i_e, j_s:j_e] = 1
                    answer[1] -= now_len**2-1
                elif arr_tmp_sum == 0:
                    quad_loc[i_s:i_e, j_s:j_e] = 1
                    answer[0] -= now_len**2-1
        now_len //= 2

    return answer


print(solution(arr1))
print(solution(arr2))