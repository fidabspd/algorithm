new_id1 = "...!@BaT#*..y.abcdefghijklm"  # "bat.y.abcdefghi"
new_id2 = "z-+.^."  # "z--"
new_id3 = "=.="  # "aaa"
new_id4 = "123_.def"  # "123_.def"
new_id5 = "abcdefghijklmn.p"  # "abcdefghijklmn"


def solution(new_id):

    import re
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    if re.search('^\.', new_id):
        new_id = new_id[1:]
    if re.search('\.$', new_id):
        new_id = new_id[:-1]
    if not new_id:
        new_id = 'a'
    new_id = new_id[:15]
    if re.search('\.$', new_id):
        new_id = new_id[:-1]
    last = new_id[-1]
    while len(new_id) < 3:
        new_id += last
        
    return new_id


print(solution(new_id1))
print(solution(new_id2))
print(solution(new_id3))
print(solution(new_id4))
print(solution(new_id5))


def solution_else(new_id):
    import re
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    