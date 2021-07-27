str11 = 'FRANCE'; str21 = 'french'  # 16384
str12 = 'handshake'; str22 = 'shake hands'  # 65536
str13 = 'aa1+aa2'; str23 = 'AAAA12'  # 43690
str14 = 'E=M*C^2'; str24 = 'e=m*c^2'  # 65536


import re
def make_elements(str_):
    str_ = re.sub(' ', '+', str_)
    en_s = re.compile('[^a-z]+')
    elements = []
    for s1, s2 in zip(str_, str_[1:]):
        e = (s1+s2).lower()
        if en_s.search(e):
            continue
        elements.append(e)
    return elements

def solution(str1, str2):
    elements1 = make_elements(str1)
    elements2 = make_elements(str2)

    union_ = len(elements1) + len(elements2)
    if union_ == 0:
        return 65536
    inter_ = 0

    for e in elements1:
        if e in elements2:
            elements2.remove(e)
            inter_ += 1
            union_ -= 1

    return int(65536*(inter_/union_))


print(solution(str11, str21))
print(solution(str12, str22))
print(solution(str13, str23))
print(solution(str14, str24))


### 참고
print('ab '.isalpha())
