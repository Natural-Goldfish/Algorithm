import sys
from collections import deque

global SAND, arr, MIN_X, MIN_Y, MAX_X, MAX_Y, ROTATION_CONTROLLER
MIN_X, MIN_Y = 0, 0
SAND = 0

DIRECTION = {
    0 : (0, -1),
    1 : (1, 0),
    2: (0, 1),
    3 : (-1, 0)
}

ROTATION_CONTROLLER = (1, 2)        # required_condition, repeat_count

def tornado(start_coord):
    global arr, DIRECTION, SAND, ROTATION_CONTROLLER
    queue = deque([start_coord])
    move_num = 0
    while True :
        y, x, direction = queue.popleft()
        if y == 0 and x == 0 : break

        dy, dx = DIRECTION[direction]
        target_y, target_x = y+dy, x+dx

        if arr[target_y][target_x] == 0 :
            move_num += 1
            if move_num == ROTATION_CONTROLLER[0] :
                move_num = 0
                ROTATION_CONTROLLER = (ROTATION_CONTROLLER[0], ROTATION_CONTROLLER[1] - 1)
                direction = (direction + 1)%4
            if ROTATION_CONTROLLER[1] == 0 :
                ROTATION_CONTROLLER = (ROTATION_CONTROLLER[0] + 1, 2)
            queue.append((target_y, target_x, direction))
            continue
        
        moved_sand = 0
        gone_sand = 0
        # 5%
        new_y, new_x = target_y + dy*2, target_x + dx*2
        if valid_coord(new_y, new_x):
            moved = 5*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved
        else :
            gone = 5*arr[target_y][target_x]//100
            gone_sand += gone

        # 10%-1
        dyy, dxx = DIRECTION[(direction+1)%4]
        new_y, new_x = target_y + dy+ dyy, target_x + dx + dxx
        if valid_coord(new_y, new_x):
            moved = 10*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved            
        else :
            gone = 10*arr[target_y][target_x]//100
            gone_sand += gone            

        # 7%-1
        new_y, new_x = target_y + dyy, target_x + dxx
        if valid_coord(new_y, new_x):
            moved = 7*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved                   
        else :
            gone = 7*arr[target_y][target_x]//100
            gone_sand += gone            

        # 2%-1
        new_y, new_x = target_y + dyy*2, target_x + dxx*2
        if valid_coord(new_y, new_x):
            moved = 2*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved 
        else :
            gone = 2*arr[target_y][target_x]//100
            gone_sand += gone            

        # 1%-1
        dyyy, dxxx = DIRECTION[(direction+2)%4]
        new_y, new_x = target_y + dyy + dyyy, target_x + dxx + dxxx
        if valid_coord(new_y, new_x):
            moved = 1*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved 
        else :
            gone = 1*arr[target_y][target_x]//100
            gone_sand += gone            

        # 10%-2
        dyy, dxx = DIRECTION[(direction-1)%4]
        new_y, new_x = target_y + dy+ dyy, target_x + dx + dxx
        if valid_coord(new_y, new_x):
            moved = 10*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved 
        else :
            gone = 10*arr[target_y][target_x]//100
            gone_sand += gone            

        # 7%-2
        new_y, new_x = target_y + dyy, target_x + dxx
        if valid_coord(new_y, new_x):
            moved = 7*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved 
        else :
            gone = 7*arr[target_y][target_x]//100
            gone_sand += gone            

        # 2%-1
        new_y, new_x = target_y + dyy*2, target_x + dxx*2
        if valid_coord(new_y, new_x):
            moved = 2*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved 
        else :
            gone = 2*arr[target_y][target_x]//100
            gone_sand += gone

        # 1%-1
        dyyy, dxxx = DIRECTION[(direction+2)%4]
        new_y, new_x = target_y + dyy + dyyy, target_x + dxx + dxxx
        if valid_coord(new_y, new_x):
            moved = 1*arr[target_y][target_x]//100
            moved_sand += moved
            arr[new_y][new_x] += moved 
        else :
            gone = 1*arr[target_y][target_x]//100
            gone_sand += gone            

        # a
        new_y, new_x = target_y + dy, target_x + dx
        if valid_coord(new_y, new_x):
            arr[new_y][new_x] += arr[target_y][target_x] - moved_sand - gone_sand
        else :
            gone_sand += arr[target_y][target_x] - moved_sand - gone_sand
            
        SAND += gone_sand
        arr[target_y][target_x] = 0

        move_num += 1
        if move_num == ROTATION_CONTROLLER[0] :
            move_num = 0
            ROTATION_CONTROLLER = (ROTATION_CONTROLLER[0], ROTATION_CONTROLLER[1] - 1)
            direction = (direction + 1)%4
        if ROTATION_CONTROLLER[1] == 0 :
            ROTATION_CONTROLLER = (ROTATION_CONTROLLER[0] + 1, 2)
        queue.append((target_y, target_x, direction))

def valid_coord(new_y, new_x):
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    if new_y < 0 or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X :
        return False
    return True


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    MAX_X, MAX_Y = N, N
    start_coord = (N//2, N//2, 0)
    arr = []
    for y in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    
    before = 0
    for y in range(N):
        before += sum(arr[y])

    
    tornado(start_coord)


    answer=0
    for y in range(N):
        answer+=sum(arr[y])

    print(before-answer)
    print(SAND)

