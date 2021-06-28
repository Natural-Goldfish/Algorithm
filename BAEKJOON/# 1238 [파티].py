import sys, heapq
from collections import deque

N, M, X = map(int, str.rstrip(sys.stdin.readline()).split(' '))
road_dict = {}
for m in range(M):
    src, dst, cost = map(int, str.rstrip(sys.stdin.readline()).split(' '))

    if src in road_dict :
        road_dict[src].append((dst, cost))
    else :
        road_dict[src] = [(dst, cost)]

go_cost, back_cost = [], []

def dijkstra(start_node, road_dict):
    costs = list(sys.maxsize for _ in range(N+1))
    costs[start_node] = 0
    heap = [(0, start_node)]

    while heap:
        _, cur_node_num = heapq.heappop(heap)
        
        for item in road_dict[cur_node_num]:
            dst_node_num, cost = item
            if costs[cur_node_num] + cost < costs[dst_node_num]:
                costs[dst_node_num] = costs[cur_node_num] + cost
                heapq.heappush(heap, (costs[dst_node_num], dst_node_num))
                
    
    return costs
temp_list = list(dijkstra(node_num, road_dict) for node_num in range(1, N+1))
answer_list = []
for index, temp in enumerate(temp_list):
    answer_list.append(temp[X] + temp_list[X-1][index+1])
print(max(answer_list))