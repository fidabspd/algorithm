s1 = "one4seveneight"  # 1478
s2 = "23four5six7"  # 234567
s3 = "2three45sixseven"  # 234567
s4 = "123"  # 123


import re
def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num, num_str in enumerate(num_list):
        s = re.sub(num_str, str(num), s)
    return int(s)


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
