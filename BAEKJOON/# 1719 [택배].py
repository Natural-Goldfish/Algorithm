import sys, heapq, copy

N, M = map(int, str.strip(sys.stdin.readline()).split(' '))
node_dict = {node : [] for node in range(N+1)}
for m in range(M):
    src, dst, time = map(int, str.strip(sys.stdin.readline()).split(' '))
    node_dict[src].append((time, dst))
    node_dict[dst].append((time, src))

def dijkstra(start, N, node_dict):
    times = [sys.maxsize for _ in range(N+1)]
    times[start] = 0
    path_info = list(list() for _ in range(N+1))
    heap = [(0, start)]
    while heap :
        _, cur_node = heapq.heappop(heap)
        if cur_node not in path_info[cur_node] :
            path_info[cur_node].append(cur_node)
        for info in node_dict[cur_node]:
            time, dst_node = info
            if times[cur_node] + time < times[dst_node] :
                times[dst_node] = times[cur_node] + time
                path_info[dst_node] = copy.deepcopy(path_info[cur_node])
                heapq.heappush(heap, (path_info[dst_node], dst_node))
    return path_info

answer_list = list(list() for _ in range(N))
for node_num in range(1, N+1):
    path_info = dijkstra(node_num, N, node_dict)[1:]
    for temp_list in path_info:
        if len(temp_list) >= 2 :
            answer_list[node_num-1].append(temp_list[1])
        else :
            answer_list[node_num-1].append(temp_list[0])
    answer_list[node_num-1][node_num-1] = '-'
for answer in answer_list:
    print(' '.join(map(str, answer)))