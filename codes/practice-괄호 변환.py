p1 = "(()())()"  # "(()())()"
p2 = ")("  # "()"
p3 = "()))((()"  # "()(())()"


def solution(p):
    if not p:
        return ''
    
    v = p
    u = ''
    left, right = 0, 0
    is_true = True
    while True:
        u += v[0]
        v = v[1:]
        
        if u[-1] == '(':
            left += 1
        else:
            right += 1
            
        if left == right:
            break  
        if left < right:
            is_true = False
            
    if is_true:
        return u + solution(v)
    
    else:
        u = ''.join(['(' if i == ')' else ')' for i in u[1:-1]])
        return '(' + solution(v) + ')' + u


print(solution(p1))
print(solution(p2))
print(solution(p3))
