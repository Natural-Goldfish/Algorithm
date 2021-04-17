from itertools import combinations
from collections import deque
import copy
global H, W, MIN_X, MIN_Y, MAX_X, MAX_Y
MIN_X, MIN_Y = 0, 0

def spread_virus(start_coord, arr):                                     # BFS
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    queue = deque([start_coord])
    while queue :
        y, x = queue.popleft()
        if arr[y][x] != 2 : continue

        # UP
        new_y, new_x = y - 1, x
        if new_y < MIN_Y or new_y >= MAX_Y : pass
        else :
            if arr[new_y][new_x] == 0 :
                arr[new_y][new_x] = 2
                queue.append((new_y, new_x))
        # DOWN
        new_y, new_x = y + 1, x
        if new_y < MIN_Y or new_y >= MAX_Y : pass
        else :
            if arr[new_y][new_x] == 0 :
                arr[new_y][new_x] = 2
                queue.append((new_y, new_x))
        # LEFT
        new_y, new_x = y, x - 1
        if new_x < MIN_X or new_x >= MAX_X : pass
        else :
            if arr[new_y][new_x] == 0 :
                arr[new_y][new_x] = 2
                queue.append((new_y, new_x))
        # RIGHT
        new_y, new_x = y, x + 1
        if new_x < MIN_X or new_x >= MAX_X : pass
        else :
            if arr[new_y][new_x] == 0 :
                arr[new_y][new_x] = 2
                queue.append((new_y, new_x))

# 0 개수 세는 function
def get_count_zero(arr):
    count = 0
    for y in range(H):
        count += len(list(filter(lambda x : x == 0, arr[y])))
    return count

# 1이 들어갈 수 있는 좌표 조합

if __name__ == "__main__":
    H, W = map(int, input().rstrip().split(' '))
    MAX_X, MAX_Y = W, H
    arr = []
    empty_coord_list = []
    virus_coord_list = []
    safety_space_num = 0

    for y in range(H):
        temp = list(map(int, input().rstrip().split(' ')))
        arr.append([])
        for x in range(len(temp)) :
            if temp[x] == 0 :
                empty_coord_list.append((y, x))
            elif temp[x] == 2 :
                virus_coord_list.append((y, x))
            arr[y].append(temp[x])
    
    cases = list(combinations(empty_coord_list, 3))
    for case in cases:
        arr_case = copy.deepcopy(arr)
        for y, x in case :
            arr_case[y][x] = 1
        
        for virus_coord in virus_coord_list:
            spread_virus(virus_coord, arr_case)
        safety_space_num = max(safety_space_num, get_count_zero(arr_case))

    print(safety_space_num)