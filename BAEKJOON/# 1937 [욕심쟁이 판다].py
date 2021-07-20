import sys

N = int(str.strip(sys.stdin.readline()))
arr = list(list(map(int, str.strip(sys.stdin.readline()).split(' '))) for _ in range(N))
path_arr = list(list(-1 for _ in range(N)) for _ in range(N))
path = 1

def dfs(coord, visited):
    global path_arr, arr, path

    visited.add(coord)
    y, x = coord
    if path_arr[y][x] == -1 :
        path_arr[y][x] = 1

    candidate = []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if y+dy < 0 or y+dy >= N or x+dx < 0 or x+dx >= N : continue
        if arr[y+dy][x+dx] <= arr[y][x] : continue

        if path_arr[y+dy][x+dx] != -1 : 
            candidate.append(path_arr[y][x]+path_arr[y+dy][x+dx])
            continue
        if (y+dy, x+dx) not in visited :
            candidate.append(path_arr[y][x] + dfs((y+dy, x+dx), visited))
            
    visited.remove(coord)
    if not candidate :
        path_arr[y][x] = 1
    else :
        path_arr[y][x] = max(path_arr[y][x], max(candidate))
        path = max(path_arr[y][x], path)
    return path_arr[y][x]

for y in range(N):
    for x in range(N):
        if path_arr[y][x] == -1 :
            dfs((y, x), set([]))
print(path)