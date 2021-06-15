import sys
from collections import deque

def bfs(queue, visited, arr):
    global W, H, C, day
    while queue :
        queue2 = deque([])

        while queue :
            w, h, c = queue.popleft()
            if (w, h, c) in visited : continue
            visited.add((w, h, c))

            # same channel
            # up, down, left, right
            dw, dh = [0, 0, -1, 1], [-1, 1, 0, 0]
            for index in range(4):
                new_w, new_h = w+dw[index], h+dh[index]
                if new_w < 0 or new_w >= W or new_h < 0 or new_h >= H :
                    pass
                else :
                    if arr[c][new_h][new_w] == 0 : 
                        arr[c][new_h][new_w] = 1
                        queue2.append((new_w, new_h, c))
            # upper channel
            if c-1 < 0 : pass
            else :
                new_c = c-1
                if arr[new_c][h][w] == 0 :
                            arr[new_c][h][w] = 1
                            queue2.append((w, h, new_c))
                        
            # down channel
            if c+1 >= C : pass
            else :
                new_c = c+1
                if arr[new_c][h][w] == 0 :
                    arr[new_c][h][w] = 1
                    queue2.append((w, h, new_c))
                        
        if queue2 :
            day += 1
        queue = queue2

def answer(arr):
    global C, H, W
    for c in range(C):
        for h in range(H):
            for w in range(W):
                if arr[c][h][w] == 0 :
                    return -1

W, H, C = map(int, str.rstrip(sys.stdin.readline(), '').split(' '))
arr = []
tasty_tomatos = deque([])
day = 0

for c in range(C):
    c_arr = []
    for h in range(H):
        temp = list(map(int, str.rstrip(sys.stdin.readline(), '').split(' ')))
        c_arr.append(temp)
        for index, item in enumerate(temp):
            if item == 1 :
                tasty_tomatos.append((index, h, c))
    arr.append(c_arr)

bfs(tasty_tomatos, set([]), arr)

if answer(arr) == -1 :
    print(-1)
else :
    print(day)