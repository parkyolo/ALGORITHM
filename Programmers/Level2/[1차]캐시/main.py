from collections import deque

def solution(cacheSize, cities):
    answer = 0

    # cache 크기가 0이면 모든 검색어에 대해 cache miss
    if cacheSize == 0:
        return len(cities)*5
    
    # 대소문자 구분 X
    cities = [i.upper() for i in cities]

    cache = deque()
    for city in cities:
        # cache hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # cache miss
        else:
            answer += 5
            # LRU 알고리즘으로 캐시 교체
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
            # cache에 추가
            else:
                cache.append(city)
                
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 50)
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]), 21)
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]), 60)
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]), 52)
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]), 16)
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 25)