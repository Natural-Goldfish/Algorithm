from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0 : return len(cities)*5
    cache, time = deque([]), 0
    for city in cities :
        city = city.lower()
        if city in cache :
            del cache[cache.index(city)]
            cache.append(city)
            time += 1
        else :
            if len(cache) == cacheSize :
                cache.popleft()
                cache.append(city)
            else :
                cache.append(city)
            time += 5
    return time