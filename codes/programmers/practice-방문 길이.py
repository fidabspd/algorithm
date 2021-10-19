dirs1 = "ULURRDLLU"  # 7
dirs2 = "LULLLLLLU"  # 7


def solution(dirs):
    move = {'U': [0,1], 'D': [0,-1], 'L': [-1,0], 'R': [1,0]}
    position = [0, 0]
    path_list = []
    for dir in dirs:
        path = [position.copy()]
        position[0] += move[dir][0]
        position[1] += move[dir][1]
        if position[0] > 5:
            position[0] = 5
        elif position[0] < -5:
            position[0] = -5
        if position[1] > 5:
            position[1] = 5
        elif position[1] < -5:
            position[1] = -5
        path.append(position.copy())
        path.sort()

        if path[0] != path[1] and path not in path_list:
            path_list.append(path)
    
    return len(path_list)


print(solution(dirs1))
print(solution(dirs2))
