import sys
from collections import deque

H, W = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = list(list(map(int, str.strip(sys.stdin.readline()).split(' '))) for _ in range(H))
paint_num, max_count = 0, 0

def bfs(start_coord):
    global arr, H, W, max_count

    queue = deque([start_coord])
    visited = set([])
    count = 0

    while queue :
        coord = queue.popleft()

        if coord in visited : continue
        visited.add(coord)
        y, x = coord
        count += 1
        arr[y][x] = 0

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            if y+dy < 0 or y+dy >= H or x+dx < 0 or x+dx >= W : continue
            if arr[y+dy][x+dx] != 1 : continue
            queue.append((y+dy, x+dx))
            
    max_count = max(max_count, count)

for y in range(H):
    for x in range(W):
        if arr[y][x] == 1 : 
            paint_num += 1
            bfs((y, x))
print(paint_num)
print(max_count)
