import sys, heapq

N = int(str.rstrip(sys.stdin.readline()))
M = int(str.rstrip(sys.stdin.readline()))
graph = [[] for _ in range(N)]
for m in range(M):
    i, j, weight = map(int, str.rstrip(sys.stdin.readline()).split(' '))
    graph[i-1].append((j-1, weight))
src, dst = map(int, str.rstrip(sys.stdin.readline()).split(' '))
distance = [sys.maxsize for _ in range(N)]
distance[src-1] = 0
def djikstra(src, distance, graph):
    pqueue = [(distance[src], src)]
    visited = set()
    while pqueue :
        cur_distance, cur_node = heapq.heappop(pqueue)
        if cur_node in visited : continue
        visited.add(cur_node)

        for info in graph[cur_node]:
            dst_node, weight = info
            if distance[cur_node] + weight < distance[dst_node] :
                distance[dst_node] = distance[cur_node] + weight
                heapq.heappush(pqueue, (distance[dst_node], dst_node))
djikstra(src-1, distance, graph)
print(distance[dst-1])