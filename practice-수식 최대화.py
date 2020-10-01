expression1 = "100-200*300-500+20"  # 60420
expression2 = "50*6-3*2"  # 300



def _split(expression):

    new = []
    tmp = ''

    for idx, e in enumerate(expression):
        tmp += e
        if e in '*+-':
            new.append(tmp[:-1])
            new.append(e)
            tmp = ''
    new.append(tmp)

    return new


def mk_ex_s(expression, _order):
    
    ex_s = _split(expression)

    for o in _order:
        while o in ex_s:
            idx = ex_s.index(o)
            if o == '*':
                ex_s[idx-1] = int(ex_s.pop(idx+1)) * int(ex_s.pop(idx-1))
            elif o == '+':
                ex_s[idx-1] = int(ex_s.pop(idx+1)) + int(ex_s.pop(idx-1))
            elif o == '-':
                ex_s[idx-1] = -int(ex_s.pop(idx+1)) + int(ex_s.pop(idx-1))
            
    return ex_s[0]

def solution(expression):
    
    from itertools import permutations

    order_set = list(permutations(['*', '+', '-']))
    
    result = []    
    for _order in order_set:
        result.append(mk_ex_s(expression, _order))
        
    result = [abs(i) for i in result]
    
    return max(result)

    
    
print(solution(expression1))
print(solution(expression2))