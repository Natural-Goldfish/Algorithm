import sys
import heapq
from itertools import permutations, product

N, E = map(int, str.strip(sys.stdin.readline()).split(' '))

graph = {n : [] for n in range(1, N+1)}

for _ in range(E):
    src, dst, distance = map(int, str.strip(sys.stdin.readline()).split(' '))
    if src not in graph :
        graph[src] = [(dst, distance)]
    else :
        graph[src].append((dst, distance))
    
    if dst not in graph :
        graph[dst] = [(src, distance)]
    else :
        graph[dst].append((src, distance))

must_node1, must_node2 = map(int, str.strip(sys.stdin.readline()).split(' '))

def dijkstra(start_node, graph, N):
    distances = [sys.maxsize for _ in range(N+1)]
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq :
        _, cur_node = heapq.heappop(pq)

        for next_node, distance in graph[cur_node]:
            if distances[cur_node] + distance < distances[next_node] :
                distances[next_node] = distances[cur_node] + distance
                heapq.heappush(pq, (distances[next_node], next_node))
    
    return distances

answer = dijkstra(1, graph, N)[must_node1] + dijkstra(must_node1, graph, N)[must_node2] + dijkstra(must_node2, graph, N)[N]
answer2 = dijkstra(1, graph, N)[must_node2] + dijkstra(must_node2, graph, N)[must_node1] + dijkstra(must_node1, graph, N)[N]
answer = min(answer, answer2)
if answer >= sys.maxsize :
    print(-1)
else :
    print(answer)
