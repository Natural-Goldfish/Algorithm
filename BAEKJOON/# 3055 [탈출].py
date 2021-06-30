import sys, copy
from collections import deque 

H, W = map(int, str.strip(sys.stdin.readline()).split(' '))

position, goal = (None, None), (None, None)
arr = []
for h in range(H):
    temp_list = list(map(str, str.strip(sys.stdin.readline())))
    for w in range(W):
        if temp_list[w] == 'S' :
            position = (h, w)
        if temp_list[w] == 'D' :
            goal = (h, w)
    arr.append(temp_list)

def rain_controller(arr, ready='*', ready_flag=False, rain='+', rain_flag=False):
    new_arr = copy.deepcopy(arr)
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == ready and ready_flag :
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if y+dy < 0 or y+dy >= len(arr) or x+dx < 0 or x+dx >= len(arr[0]):continue
                    if arr[y+dy][x+dx] == '.' :
                        new_arr[y+dy][x+dx] = '+'
            if arr[y][x] == rain and rain_flag :
                new_arr[y][x] = '*'
    return new_arr

queue = deque([position])
visited = set([])
answer, answer_flag = 0, False
while queue :
    temp_queue = []
    arr = rain_controller(arr, ready_flag=True)
    while queue :
        cur_position = queue.popleft()
        y, x = cur_position
        if cur_position == goal :
            answer_flag = True
            temp_queue = []
            break
        if cur_position in visited : continue
        visited.add(cur_position)
        
        
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if y+dy < 0 or y+dy >= len(arr) or x+dx < 0 or x+dx >= len(arr[0]):continue
            if arr[y+dy][x+dx] == '.' or arr[y+dy][x+dx] == 'D':
                temp_queue.append((y+dy, x+dx))
    arr = rain_controller(arr, rain_flag=True)
    if temp_queue :
        queue = deque(temp_queue)
        answer += 1
    if answer_flag : break
if answer_flag :
    print(answer)
else :
    print('KAKTUS')