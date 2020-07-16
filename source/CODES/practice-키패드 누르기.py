numbers1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]; hand1 = "right"  # "LRLLLRLLRRL"
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]; hand2 = "left"  # "LRLLRRLLLRR"
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]; hand3 = "right"  # "LLRLLRLLRL"


def solution(numbers, hand):
    result = ''
    left = [3, 0]; right = [3, 2]
    for num in numbers:

        if num == 0:
            row = 3; col = 1
        else:
            row = (num-1) // 3; col = (num-1) % 3

        if col == 0:
            left = [row, col]
            tmp = 'L'
        elif col == 2:
            right = [row, col]
            tmp = 'R'
        else:
            dist_L = abs(row - left[0]) + abs(col - left[1])
            dist_R = abs(row - right[0]) + abs(col - right[1])
            #print('dist_L:', dist_L, 'dist_R:', dist_R)
            if dist_L > dist_R:
                right = [row, col]
                tmp = 'R'
            elif dist_L < dist_R:
                left = [row, col]
                tmp = 'L'
            else:
                if hand == 'left':
                    left = [row, col]
                    tmp = 'L'
                else:
                    right = [row, col]
                    tmp = 'R'
        result += tmp
        #print(num, 'num:', [row, col], ', left:', left, ', right:', right, 'hand:', tmp)
        
    return result

print(solution(numbers1, hand1), '\n\n')
print(solution(numbers2, hand2), '\n\n')
print(solution(numbers3, hand3), '\n\n')