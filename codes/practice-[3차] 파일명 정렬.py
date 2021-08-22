files1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
files2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]


import re
def solution(files):
    pattern = re.compile('([^0-9]+)([0-9]+)([a-zA-Z0-9 .-]*)')
    sort_dict = {}
    for file in files:
        sort_dict[file] = {}
        mat = pattern.search(file)
        sort_dict[file]['HEAD'] = mat.group(1).lower()
        sort_dict[file]['NUMBER'] = int(mat.group(2))
    files = sorted(files, key=lambda file: sort_dict[file]['NUMBER'])
    files = sorted(files, key=lambda file: sort_dict[file]['HEAD'])
    return files


print(solution(files1))
print(solution(files2))


def solution_else(files):
    pattern = re.compile('([^0-9]+)([0-9]+)')
    return sorted(files, key=lambda file: (pattern.findall(file)[0][0].lower(), int(pattern.findall(file)[0][1])))
