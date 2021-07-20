import sys
from collections import deque

H, W = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = []
for y in range(H):
    arr.append(list(map(int, str.strip(sys.stdin.readline()))))


def bfs(y, x):
    queue = deque([(y, x, False)])
    visited = set()
    count = 1

    while queue :
        temp_queue = deque([])
        while queue :
            y, x, chance = queue.pop()

            if (y, x, chance) in visited : continue
            if y == H-1 and x == W-1 :
                return count

            visited.add((y, x, chance))

            for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                if y+dy < 0 or y+dy >= H or x+dx < 0 or x+dx >= W : continue
                if arr[y+dy][x+dx] == 1 and chance == True : continue
                if arr[y+dy][x+dx] == 1 and chance == False :
                    temp_queue.append((y+dy, x+dx, True))
                    continue
                else :
                    temp_queue.append((y+dy, x+dx, chance))
        if temp_queue :
            queue = temp_queue
            count += 1
        
count = bfs(0, 0)
if count == None :
    print(-1)
else :
    print(count)

'''
def dfs(coord, chance):
    global visited, path, arr

    y, x = coord
    visited[y][x] = 1

    if y == H-1 and x == W-1 : 
        visited[y][x] = 0
        path[y][x] = 1        
        return (path[y][x], True)

    find = False
    for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        if y+dy < 0 or y+dy >= H or x+dx < 0 or x+dx >= W : continue
        if arr[y+dy][x+dx] == 1 and chance == 1 : continue
        if visited[y+dy][x+dx] == 1 : continue
        if path[y+dy][x+dx] == -1 : continue
        if path[y+dy][x+dx] < path[y][x] : 
            path[y][x] = path[y+dy][x+dx] + 1
            continue
        if arr[y+dy][x+dx] == 1 and chance == 0:
            return_path, flag = dfs((y+dy, x+dx), chance+1)
            if flag == True :
                path[y][x] = min(path[y][x], return_path+1)
                find = True
        elif arr[y+dy][x+dx] == 0 and chance == 0:
            return_path, flag = dfs((y+dy, x+dx), chance)
            if flag == True :
                path[y][x] = min(path[y][x], return_path+1)
                find = True
        elif arr[y+dy][x+dx] == 0 and chance == 1:
            return_path, flag = dfs((y+dy, x+dx), chance)
            if flag == True :
                path[y][x] = min(path[y][x], return_path+1)
                find = True

    visited[y][x] = 0
    if find :
        return (path[y][x], True)
    path[y][x] = -1
    return (path[y][x], False)

def dfs(coord, path, chance, arr):
    global visited
    y, x = coord
    path += 1
    visited[y][x] = 1

    if y == H-1 and x == W-1 :
        value, origin_path, _, _ = arr[y][x]
        if origin_path < path : pass
        else :
            arr[y][x] = (value, path, chance, True)
            visited.remove((y, x))
            return True

    value, _, _, _ = arr[y][x]
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if y+dy < 0 or y+dy >= H or x+dx < 0 or x+dx >= W : continue
        if arr[y+dy][x+dx][0] == 1 and chance == 1 : continue
        if visited[y+dy][x+dx] == 1 : continue

        if arr[y+dy][x+dx][0] == 1 and chance == 0 and arr[y+dy][x+dx][1] > path+1:
            if dfs((y+dy, x+dx), path, chance+1, arr) :
                arr[y][x] = (value, path, chance, True)
        elif arr[y+dy][x+dx][0] == 0 and arr[y+dy][x+dx][1] > path+1 :
            if dfs((y+dy, x+dx), path, chance, arr) :
                arr[y][x] = (value, path, chance, True)

    
    visited[y][x] = 0
    return arr[y][x][3]

dfs((0, 0), 0)
if path[0][0] == sys.maxsize :
    print(-1)
else :
    print(path[0][0])

'''

[1, 2,3]
[2, 3, 4]
[0, 4, 5]