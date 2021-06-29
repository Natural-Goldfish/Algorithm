import sys, heapq, copy

N = int(str.strip(sys.stdin.readline()))
M = int(str.strip(sys.stdin.readline()))
city_dict = {city_num : [] for city_num in range(N+1)}
for m in range(M):
    src, dst, cost = map(int, str.strip(sys.stdin.readline()).split(' '))
    city_dict[src].append((cost, dst))
src_city, dst_city = map(int, str.strip(sys.stdin.readline()).split(' '))

def dijkstra(src_city, N, city_dict):
    heap = [(0, src_city)]
    costs = [sys.maxsize for _ in range(N+1)]
    costs[src_city] = 0
    path_info = list(list() for _ in range(N+1))

    while heap :
        _, src_city = heapq.heappop(heap)
        if src_city not in path_info[src_city] :
            path_info[src_city].append(src_city)

        for info in city_dict[src_city]:
            cost, dst_city = info
            if costs[src_city] + cost < costs[dst_city] :
                costs[dst_city] = costs[src_city] + cost
                path_info[dst_city] = copy.deepcopy(path_info[src_city])
                heapq.heappush(heap, (costs[dst_city], dst_city))
    return costs, path_info
costs, path_info = dijkstra(src_city, N, city_dict)
# for cost in costs :
#     print(cost)
print(costs[dst_city])
print(len(path_info[dst_city]))
print(' '.join(map(str, path_info[dst_city])))