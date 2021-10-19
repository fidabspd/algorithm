skill = "CBD"; skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]  # 2

def solution(skill, skill_trees):
    answer = len(skill_trees)
    for user_skill in skill_trees:
        skill_list = list(skill)
        for sk in user_skill:
            if sk in skill:
                if sk == skill_list[0]:
                    skill_list.pop(0)
                else:
                    answer -= 1
                    break
            
    return answer

print(solution(skill, skill_trees))