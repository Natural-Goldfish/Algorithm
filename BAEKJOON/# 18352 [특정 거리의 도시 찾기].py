import sys, heapq

N, M, K, X = map(int, str.strip(sys.stdin.readline()).split(' '))
# N : 도시의 수
# X : 출발 도시 번호
# K : 출발 도시에서의 도달 할 수 있는 도시 중, 최단 거리
road_dict = {city_num : [] for city_num in range(1, N+1)}

for m in range(M):
    src, dst = map(int, str.strip(sys.stdin.readline()).split(' '))
    if src in road_dict :
        road_dict[src].append((1, dst))

def dijkstra(start_city_num, road_dict, N):
    costs = list(sys.maxsize for _ in range(N+1))
    costs[start_city_num] = 0
    heap = [(0, start_city_num)]

    while heap :
        _, cur_city_num = heapq.heappop(heap)

        for cost, dst_city_num in road_dict[cur_city_num]:
            if costs[cur_city_num] + cost < costs[dst_city_num] :
                costs[dst_city_num] = costs[cur_city_num] + cost
                heapq.heappush(heap, (costs[dst_city_num], dst_city_num))
    return costs
costs = dijkstra(X, road_dict, N)
answer_list = list(filter(lambda x: x[0] == K, list(zip(costs, list(index for index in range(len(costs)))))))
if not answer_list : print(-1)
else :
    for answer in answer_list:
        print(answer[1])
