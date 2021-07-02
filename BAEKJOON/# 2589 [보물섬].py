import sys, heapq

H, W = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = list(list(map(str, str.strip(sys.stdin.readline()))) for _ in range(H))
answers = list(list(0 for _ in range(len(arr[0]))) for _ in range(len(arr)))
def dijkstra(coord, arr):
    distances = list(list(sys.maxsize for _ in range(len(arr[0]))) for _ in range(len(arr)))
    distances[coord[0]][coord[1]] = 0
    pq = [(0, coord)]
    while pq :
        _, coord = heapq.heappop(pq)
        y, x = coord
        answers[y][x] = max(answers[y][x], distances[y][x])

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y, new_x = y+dy, x+dx
            if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]) : continue
            if arr[new_y][new_x] == 'L' and distances[y][x] + 1 < distances[new_y][new_x]:
                distances[new_y][new_x] = distances[y][x] + 1
                heapq.heappush(pq, (distances[new_y][new_x], (new_y, new_x)))
    
for y in range(H):
    for x in range(W):
        if arr[y][x] == 'L' :
            dijkstra((y, x), arr)
answer = 0        
for temp_list in answers :
    answer = max(max(temp_list), answer)
print(answer)
    

