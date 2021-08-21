cacheSize1 = 3; cities1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]  # 50
cacheSize2 = 3; cities2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]  # 21
cacheSize3 = 2; cities3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]  # 60
cacheSize4 = 5; cities4 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]  # 52
cacheSize5 = 2; cities5 = ["Jeju", "Pangyo", "NewYork", "newyork"]  # 16
cacheSize6 = 0; cities6 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]  # 25


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
        cache.append(city)
        cache = cache[-cacheSize:]
    return answer


print(solution(cacheSize1, cities1))
print(solution(cacheSize2, cities2))
print(solution(cacheSize3, cities3))
print(solution(cacheSize4, cities4))
print(solution(cacheSize5, cities5))
print(solution(cacheSize6, cities6))
