import sys, heapq

N = int(str.strip(sys.stdin.readline()))
M = int(str.strip(sys.stdin.readline()))
bus_dict = {bus_num : [] for bus_num in range(N+1)}
for m in range(M):
    src, dst, cost = map(int, str.strip(sys.stdin.readline()).split(' '))
    bus_dict[src].append((cost, dst))

def dijkstra(start, bus_dict, N):
    costs = [sys.maxsize for _ in range(N+1)]
    costs[start] = 0

    pq = [(0, start)]
    while pq :
        _, city = heapq.heappop(pq)

        for cost, dst_city in bus_dict[city]:
            if costs[city] + cost < costs[dst_city] :
                costs[dst_city] = costs[city] + cost
                heapq.heappush(pq, (costs[dst_city], dst_city))
    return costs
answer_list = []
for city in range(1, N+1):
    costs = dijkstra(city, bus_dict, N)[1:]
    answer_list.append(' '.join(list(map(lambda x: str(0) if x == sys.maxsize else str(x), costs))))
for answer in answer_list :
    print(answer)

