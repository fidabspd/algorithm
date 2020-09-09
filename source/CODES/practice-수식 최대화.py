expression1 = "100-200*300-500+20"  # 60420
expression2 = "50*6-3*2"  # 300
expression = expression1


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

print(_split(expression))