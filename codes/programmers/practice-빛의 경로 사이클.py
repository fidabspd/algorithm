grid1 = ["SL","LR"]  # [16]
grid2 = ["S"]  # [1,1,1,1]
grid3 = ["R","R"]  # [4,4]


def solution(grid):

    answer = []

    # top, right, bottom, left
    w = len(grid[0])
    h = len(grid)
    visited = [[[[False for _ in range(2)] for _ in range(4)] for _ in range(w)] for _ in range(h)]

    turn = {'L': 1, 'S': 2, 'R': 3}
    direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

    for i in range(h):
        for j in range(w):
            for d in range(4):
                cycle = []
                if not visited[i][j][d][0]:
                    while True:
                        ijds = str(i)+'-'+str(j)+'-'+str(d)+'-'+'0'
                        if len(cycle) > 0 and cycle[0] == ijds:
                            answer.append(len(cycle)//2)
                            break
                        cycle.append(ijds)
                        visited[i][j][d][0] = True
                        d = (d+turn[grid[i][j]])%4
                        ijds = str(i)+'-'+str(j)+'-'+str(d)+'-'+'1'
                        cycle.append(ijds)
                        visited[i][j][d][1] = True
                        i, j = (i+direction[d][0])%h, (j+direction[d][1])%w
                        d = (d+2)%4

    return sorted(answer)


print(solution(grid1))
print(solution(grid2))
print(solution(grid3))