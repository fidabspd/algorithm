strings1 = ["sun", "bed", "car"]; n1 = 1  # ["car", "bed", "sun"]
strings2 = ["abce", "abcd", "cdx"]; n2 = 2  # ["abcd", "abce", "cdx"]

def solution(strings, n):
    answer = sorted(strings, key = lambda x: (x[n], x))
    return answer

print(solution(strings1, n1))
print(solution(strings2, n2))