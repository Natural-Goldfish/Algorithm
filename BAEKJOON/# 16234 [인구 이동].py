import sys
from collections import deque 

def open_or_not(N):
    open_arr, flag = list(list(0 for _ in range(N)) for _ in range(N)), False
    unique_id = 1
    for y in range(N):
        for x in range(N):
            if open_arr[y][x] == 0 :
                if bfs((y, x), open_arr, unique_id, True) :
                    flag = True
                unique_id += 1
    return open_arr, flag

def move(arr, open_arr, N):
    for y in range(N):
        for x in range(N):
            if open_arr[y][x] != 0 :
                unique_id = open_arr[y][x]
                alliance = list(bfs((y, x), open_arr, unique_id))

                summary = 0
                for new_y, new_x in alliance :
                    summary += arr[new_y][new_x]
                new_population = int(summary/len(alliance))
                for new_y, new_x in alliance :
                    arr[new_y][new_x] = new_population

def bfs(start, open_arr, unique_id, open_or_not=False):
    queue = deque([start])
    visited = set([])
    flag = False
    while queue :
        cur = queue.popleft()
        if cur in visited : continue
        visited.add(cur)
        y, x = cur
        if not open_or_not :
            open_arr[y][x] = 0
            for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if y+dy < 0 or y+dy >= N or x+dx < 0 or x+dx >= N : continue
                if open_arr[y+dy][x+dx] == unique_id :
                    queue.append((y+dy, x+dx))
        else :
            open_arr[y][x] = unique_id
            for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if y+dy < 0 or y+dy >= N or x+dx < 0 or x+dx >= N : continue
                if L <= abs(arr[y][x]-arr[y+dy][x+dx]) <= R :
                    queue.append((y+dy, x+dx))
                    flag = True
    if not open_or_not :
        return visited
    else :
        return flag


N, L, R = map(int, str.strip(sys.stdin.readline()).split(' '))
arr = list(list(map(int, str.strip(sys.stdin.readline()).split(' '))) for _ in range(N))
answer = 0
while True :
    open_arr, flag = open_or_not(N)
    if not flag : break
    move(arr, open_arr, N)
    answer += 1
print(answer)