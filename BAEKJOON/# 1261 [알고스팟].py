import sys, heapq

N, M = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = list(list(map(int, ' '.join(str.strip(sys.stdin.readline())).split(' '))) for _ in range(M))

connect_dict = {}

for y in range(M):
    for x in range(N):
        connect_dict[(y, x)] = []
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if y+dy < 0 or y+dy >= M or x+dx <0 or x+dx >= N :
                pass
            else :
                if arr[y+dy][x+dx] == 1 :
                    connect_dict[(y, x)].append((1, (y+dy, x+dx)))
                else :
                    connect_dict[(y, x)].append((0, (y+dy, x+dx)))

def dijkstra(connect_dict):
    global N, M
    
    costs = list(list(sys.maxsize for _ in range(N)) for _ in range(M))
    heap = [(0, (0, 0))]
    costs[0][0] = 0

    while heap :
        _, src_coord = heapq.heappop(heap)
        

        for item in connect_dict[src_coord]:
            cost, dst_coord = item
            if costs[src_coord[0]][src_coord[1]] + cost < costs[dst_coord[0]][dst_coord[1]] :
                costs[dst_coord[0]][dst_coord[1]] = costs[src_coord[0]][src_coord[1]] + cost
                heapq.heappush(heap, (costs[dst_coord[0]][dst_coord[1]], dst_coord))
    return costs

costs = dijkstra(connect_dict)

print(costs[M-1][N-1])

    


                
                
