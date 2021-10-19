s1 = 'a234'  # false
s2 = '1234'  # true

def solution(s):
    try:
        if len(s) in (4, 6):
            s = int(s)
            return True
        else:
            return False
    except:
        return False

print(solution('12345a'))


# 참고
s = '123a'
print(s.isdigit())