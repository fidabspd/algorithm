n1 = 5; arr11 = [9, 20, 28, 18, 11]; arr21 = [30, 1, 21, 17, 28]  # ["#####","# # #", "### #", "# ##", "#####"]
n2 = 6; arr12 = [46, 33, 33 ,22, 31, 50]; arr22 = [27 ,56, 19, 14, 14, 10]  # ["######", "### #", "## ##", " #### ", " #####", "### # "]


def convert_2(integer_, n):
    arr_2 = []
    while integer_ != 0:
        arr_2 = [integer_%2] + arr_2
        integer_ //= 2
    return [0]*(n-len(arr_2))+arr_2

def solution(n ,arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(''.join([' ' if one+two == 0 else '#' for one, two in zip(convert_2(arr1[i], n), convert_2(arr2[i], n))]))
    return answer


print(solution(n1, arr11, arr21))
print(solution(n2, arr12, arr22))


def solution_else(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
