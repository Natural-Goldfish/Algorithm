import sys, copy
from collections import deque

def bfs(arr, start_point):
    queue = deque([start_point])
    color = arr[start_point[0]][start_point[1]]
    visited = set()
    while queue :
        y, x = queue.popleft()
        if (y, x) in visited :
            continue
        visited.add((y, x))
        arr[y][x] = None

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            if y+dy < 0 or y+dy >= N or x+dx < 0 or x+dx >= N : continue
            if arr[y+dy][x+dx] == color :
                queue.append((y+dy, x+dx))

N = int(str.rstrip(sys.stdin.readline()))
arr = list(list(map(str, str.rstrip(sys.stdin.readline()))) for n in range(N))
arr2 = copy.deepcopy(arr)

for y in range(N):
    for x in range(N):
        if arr2[y][x] == 'G':
            arr2[y][x] = 'R'

count, count2 = 0, 0
for y in range(N):
    for x in range(N):
        if arr[y][x] is not None :
            bfs(arr, (y, x))
            count += 1

        if arr2[y][x] is not None :
            bfs(arr2, (y, x))
            count2 += 1
print(count, count2)


