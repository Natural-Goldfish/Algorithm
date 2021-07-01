import sys, copy
from collections import deque

H, W = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = list(list(map(int, str.strip(sys.stdin.readline()).split(' '))) for _ in range(H))

def count_ice(arr, H, W):
    temp_arr = copy.deepcopy(arr)
    count = 0
    for y in range(H):
        for x in range(W):
            if temp_arr[y][x] != 0 :
                bfs((y, x), temp_arr)
                count += 1
    return count
def bfs(start, arr):
    queue = deque([start])
    visited = set([])
    while queue :
        cur = queue.popleft()

        if cur in visited : continue
        visited.add(cur)
        y, x = cur
        arr[y][x] = 0

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if y+dy < 0 or y+dy >= len(arr) or x+dx < 0 or x+dx >= len(arr[0]):continue
            if arr[y+dy][x+dx] != 0 :
                queue.append((y+dy, x+dx))

def ice_controller(arr):
    temp_arr = list(list(0 for _ in range(W)) for _ in range(H))
    flag = False
    for y in range(H):
        for x in range(W):
            if arr[y][x] != 0 :
                for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if y+dy < 0 or y+dy >= len(arr) or x+dx < 0 or x+dx >= len(arr[0]):continue
                    if arr[y+dy][x+dx] == 0 :
                        temp_arr[y][x] += 1
                        flag = True
    return temp_arr, flag

def ice_melt(arr, temp_arr):
    for y in range(H):
        for x in range(W):
            if temp_arr[y][x] != 0 :
                arr[y][x] = max(0, arr[y][x] - temp_arr[y][x])


time = 0
while True :
    cur_ice = count_ice(arr, H, W)
    temp_arr, flag = ice_controller(arr)
    if cur_ice == 0 and flag == False : 
        break
    if cur_ice >= 2 and flag == True :
        break
    ice_melt(arr, temp_arr)
    time += 1
if flag :
    print(time)
else :
    print(0)
