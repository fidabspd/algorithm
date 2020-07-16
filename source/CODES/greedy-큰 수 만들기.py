number1 = "1924"; k1 = 2  # "94"
number2 = "1231234"; k2 = 3  # "3234"
number3 = "4177252841"; k3 = 4  # "775841"


### 시간초과
def solution(number, k):
    number_list = list(number)
    
    for idx, num in enumerate(number):
        for comp in number[idx+1:idx+1+k]:
            if num < comp:
                number_list.remove(num)
                k -= 1
                break
        if k == 0:
            break
            
    if k != 0:
        number_list = number_list[:-k]
        
    return ''.join(number_list)
            
print(solution(number1, k1))
print(solution(number2, k2))
print(solution(number3, k3))

print(solution('987654321', 3))