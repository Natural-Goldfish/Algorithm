from itertools import product
import copy
from collections import deque

global MIN_X,MIN_Y, MAX_X, MAX_Y
MIN_X, MIN_Y = 0, 0

possible_direction = {
    1 : [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],
    2 : [(1, 1, 0, 0), (0, 0, 1, 1)],
    3 : [(1, 0, 0, 1), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0)],
    4 : [(1, 0, 1, 1), (1, 1, 0, 1), (0, 1, 1, 1), (1, 1, 1, 0)],
    5 : [(1, 1, 1, 1)]
}

def BFS(info, office):
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    queue = deque([info])
    while queue :
        y, x, direction = queue.popleft()
        flag_u, flag_d, flag_l, flag_r = direction
        office[y][x] = -1

        # UP
        if flag_u :
            new_y, new_x = y - 1, x
            if new_y < MIN_Y or new_y >= MAX_Y : pass
            else :
                if office[new_y][new_x] == 6 : pass
                else : # Camera or Light or Empty
                    new_direction = (1, 0, 0, 0)
                    queue.append((new_y, new_x, new_direction))
        # DOWN
        if flag_d :
            new_y, new_x = y + 1, x
            if new_y < MIN_Y or new_y >= MAX_Y : pass
            else :
                if office[new_y][new_x] == 6 : pass
                else : # Camera or Light or Empty
                    new_direction = (0, 1, 0, 0)
                    queue.append((new_y, new_x, new_direction))            
        # LEFT
        if flag_l :
            new_y, new_x = y, x - 1
            if new_x < MIN_X or new_x >= MAX_X : pass
            else :
                if office[new_y][new_x] == 6 : pass
                else : # Camera or Light or Empty
                    new_direction = (0, 0, 1, 0)
                    queue.append((new_y, new_x, new_direction))
        # RIGHT
        if flag_r :
            new_y, new_x = y, x + 1
            if new_x < MIN_X or new_x >= MAX_X : pass
            else :
                if office[new_y][new_x] == 6 : pass
                else : # Camera or Light or Empty
                    new_direction = (0, 0, 0, 1)
                    queue.append((new_y, new_x, new_direction))

def find_zero(office):
    global MAX_Y
    count = 0
    for y in range(MAX_Y):
        count += len(list(filter(lambda x : x == 0, office[y])))
    return count

if __name__ == "__main__":
    H, W = map(int, input().rstrip().split(' '))
    MAX_X, MAX_Y = W, H
    temp_case = []
    office = []
    for y in range(H):
        numbers = list(map(int, input().rstrip().split(' ')))

        for x in range(W):
            if numbers[x] != 6 and numbers[x] != 0 :
                temp = []
                for direction in possible_direction[numbers[x]]:
                    temp.append((y, x, direction))
                temp_case.append(temp)
        office.append(numbers)
    
    possible_cases = product(*temp_case)
    min_count = MAX_X * MAX_Y + 1
    for case in possible_cases:
        office_case = copy.deepcopy(office)
        
        for info in case :
            BFS(info, office_case)
        min_count = min(min_count, find_zero(office_case))
    print(min_count)
