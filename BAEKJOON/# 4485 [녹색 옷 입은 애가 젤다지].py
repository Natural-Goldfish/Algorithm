import sys, heapq

def dijkstra(start_coord, N, arr):
    costs = list(list(sys.maxsize for _ in range(N)) for _ in range(N))
    costs[start_coord[0]][start_coord[1]] = 0
    heap = [(0, start_coord)]

    while heap :
        _, cur_coord = heapq.heappop(heap)
        y, x = cur_coord
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if y+dy < 0 or y+dy >= N or x+dx < 0 or x+dx >= N: continue
            if costs[y][x] + arr[y+dy][x+dx] < costs[y+dy][x+dx] :
                costs[y+dy][x+dx] = costs[y][x] + arr[y+dy][x+dx]
                heapq.heappush(heap, (costs[y+dy][x+dx], (y+dy, x+dx)))
    return costs

answer_list = []
while True :
    N = int(str.strip(sys.stdin.readline()))
    if N == 0 : break
    arr = list(list(map(int, str.rstrip(sys.stdin.readline()).split(' '))) for _ in range(N))

    costs = dijkstra((0, 0), N, arr)
    answer_list.append(costs[-1][-1] + arr[0][0])

for index, answer in enumerate(answer_list):
    print(f'Problem {index+1}: {answer}')

