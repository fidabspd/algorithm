scores1 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]  # "FBABD"
scores2 = [[50,90],[50,87]]  # "DA"
scores3 = [[70,49,90],[68,50,38],[73,31,100]]  # "CFD"


def solution(scores):
    scores = [list(score) for score in zip(*scores)]
    grades = ''
    for i, score in enumerate(scores):
        my_score = score[i]
        if (max(score) == my_score or min(score) == my_score) and (score.count(my_score) == 1):
            score.remove(my_score)
        grade = sum(score)/len(score)
        if grade >= 90:
            grade = 'A'
        elif grade >= 80:
            grade = 'B'
        elif grade >= 70:
            grade = 'C'
        elif grade >= 50:
            grade = 'D'
        else:
            grade = 'F'
        grades += grade
    return grades


print(solution(scores1))
print(solution(scores2))
print(solution(scores3))