W = 8; H = 12  # 80

def solution(W, H):

    i = min(W, H)
    while True:
        if (W%i) + (H%i) == 0:
            break
        i -= 1
    tmp = [W//i, H//i]
    
    return W*H - (max(tmp) + min(tmp) - 1) * i

print(solution(W, H))