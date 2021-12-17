a = [1, 2, 5, 4, 3]; b = [5, 5, 6, 6, 5]; k = 3


def swap_elements(a, b, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    return sum(a)


print(swap_elements(a, b, k))