park0 = ["SOO", "OOO", "OOO"]
routes0 = ["E 2", "S 2", "W 1"]  # [2,1]
park1 = ["SOO", "OXX", "OOO"]
routes1 = ["E 2", "S 2", "W 1"]  # [0,1]
park2 = ["OSO", "OOO", "OXO", "OOO"]
routes2 = ["E 2", "S 3", "W 1"]  # [0,0]


def solution(park, routes):
    def get_start_point():
        for i in range(park_height):
            for j in range(park_width):
                if park[i][j] == "S":
                    return i, j

    def is_valid_check_point(i, j):
        if not 0 <= i < park_height:
            return False
        elif not 0 <= j < park_width:
            return False
        elif park[i][j] == "X":
            return False
        else:
            return True

    def move(start_i, start_j, d, n):
        end_i, end_j = start_i, start_j
        move_i, move_j = move_dict[d]
        for _ in range(n):
            end_i += move_i
            end_j += move_j
            if not is_valid_check_point(end_i, end_j):
                return start_i, start_j
        return end_i, end_j

    move_dict = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }
    park_height, park_width = len(park), len(park[0])

    point = get_start_point()
    for route in routes:
        d, n = route.split(" ")
        n = int(n)
        point = move(*point, d, n)

    return list(point)


print(solution(park0, routes0))
print(solution(park1, routes1))
print(solution(park2, routes2))
