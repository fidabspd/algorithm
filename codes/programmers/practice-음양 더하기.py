absolutes1 = [4,7,12]; signs1 = [True,False,True]  # 9
absolutes2 = [1,2,3]; signs2 = [False,False,True]  # 0

def solution(absolutes, signs):
    return sum([i if j else -i for i, j in zip(absolutes, signs)])

print(solution(absolutes1, signs1))
print(solution(absolutes2, signs2))