import sys, copy
from collections import deque 

H, W = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = list(list(map(str, str.strip(sys.stdin.readline()))) for _ in range(H))

def bfs(start_coord, arr):
    queue = deque([start_coord])
    visited = set([])
    lamb, wolf = 0, 0

    while queue :
        coord = queue.popleft()
        if coord in visited : continue
        visited.add(coord)
        y, x = coord

        if arr[y][x] == 'v' :
            wolf += 1
        elif arr[y][x] == 'o' :
            lamb += 1
        
        arr[y][x] = '#'

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dy+y < 0 or dy+y >= H or dx+x < 0 or dx+x >= W : continue
            if arr[dy+y][dx+x] != '#' :
                queue.append((dy+y, dx+x))
    return lamb, wolf

alive_lamb, alive_wolf = 0, 0
for y in range(H):
    for x in range(W):
        if arr[y][x] != '#':
            lamb, wolf = bfs((y, x), arr)
            if lamb > wolf :
                alive_lamb += lamb
            else :
                alive_wolf += wolf
print(f'{alive_lamb} {alive_wolf}')