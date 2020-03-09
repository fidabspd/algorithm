def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
                return False
    return True


print(solution(["123", "456", "789"]))
print(solution(["123", "456", "12"]))