key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def solution(key, lock):
    
    m = len(key)
    n = len(lock)
    
    def rotate_right(key):
        return [list(k[::-1]) for k in zip(*key)]
    
    def move_key(key, i, j):
        if i > 0:
            key = [[0]*i + k[:n-i] for k in key]
        else:
            key = [k[-i:] + [0]*(n-m-i) for k in key]
        if j > 0:
            key = [[0]*n]*j + key[:n-j]
        else:
            key = key[-j:] + [[0]*n]*(n-m-j)
        return key
    
    def is_right(key, lock):
        for k, l in zip(key, lock):
            for k_, l_ in zip(k, l):
                if k_ + l_ != 1:
                    return False
        return True
        
    for _ in range(4):
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                moved_key = move_key(key, i, j)
                if is_right(moved_key, lock):
                    return True
        key = rotate_right(key)
    
    return False


print(solution(key, lock))