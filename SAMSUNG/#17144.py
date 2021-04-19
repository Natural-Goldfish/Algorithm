import sys, math
global MIN_X, MIN_Y, MAX_X, MAX_Y, machine_coord
MIN_X, MIN_Y = 0, 0

# 확산
def spread(arr):
    global machine_coord
    new_arr = []
    for y in range(len(arr)):
        new_arr.append([0 for _ in range(len(arr[y]))])
    
    for coord in machine_coord :
        y, x = coord
        new_arr[y][x] = -1

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if (y, x) in machine_coord : continue
            count = 0
            # UP
            dy, dx = -1, 0
            new_y, new_x = y + dy, x + dx
            if valid_coord((y, x), dy, dx) :
                if arr[new_y][new_x] != -1 and arr[y][x] != 0 :
                    split_dust = arr[y][x]//5
                    if split_dust != 0 :
                        new_arr[new_y][new_x] += split_dust
                        count += 1
            # DOWN
            dy, dx = 1, 0
            new_y, new_x = y + dy, x + dx
            if valid_coord((y, x), dy, dx) :
                if arr[new_y][new_x] != -1 and arr[y][x] != 0:
                    split_dust = arr[y][x]//5
                    if split_dust != 0 :
                        new_arr[new_y][new_x] += split_dust
                        count += 1
            # LEFT
            dy, dx = 0, -1
            new_y, new_x = y + dy, x + dx
            if valid_coord((y, x), dy, dx) :
                if arr[new_y][new_x] != -1 and arr[y][x] != 0:
                    split_dust = arr[y][x]//5
                    if split_dust != 0 :
                        new_arr[new_y][new_x] += split_dust
                        count += 1
            # RIGHT
            dy, dx = 0, 1
            new_y, new_x = y + dy, x + dx
            if valid_coord((y, x), dy, dx) :
                if arr[new_y][new_x] != -1 and arr[y][x] != 0:
                    split_dust = arr[y][x]//5
                    if split_dust != 0 :
                        new_arr[new_y][new_x] += split_dust
                        count += 1

            new_arr[y][x] += arr[y][x] - (arr[y][x]//5)*count
    return new_arr

def valid_coord(cur_coord, dy, dx):
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    y, x = cur_coord
    if y+dy < MIN_Y or y+dy >= MAX_Y or x+dx < MIN_X or x+dx >= MAX_X :
        return False
    return True
 
# 공기 청정기 작동
def machine_work(arr):
    global machine_coord

    # Counter clock-wise
    machine_y, machine_x = machine_coord[0]
    move_item, _ = arr[machine_y].pop(), arr[machine_y].pop(0)
    arr[machine_y] = [-1, 0] + arr[machine_y]
    for y in range(machine_y-1, -1, -1):
        move_item, arr[y][len(arr[y])-1] = arr[y][len(arr[y])-1], move_item
    
    for x in range(len(arr[0])-2, -1, -1):
        move_item, arr[0][x] = arr[0][x], move_item
    
    for y in range(1, machine_y):
        move_item, arr[y][0] = arr[y][0], move_item
    move_item = None

    # Clock-wise
    machine_y, machine_x = machine_coord[1]
    move_item, _ = arr[machine_y].pop(), arr[machine_y].pop(0)
    arr[machine_y] = [-1, 0] + arr[machine_y]
    for y in range(machine_y+1, len(arr)):
        move_item, arr[y][len(arr[y])-1] = arr[y][len(arr[y])-1], move_item

    for x in range(len(arr[0])-2, -1, -1):
        move_item, arr[len(arr)-1][x] = arr[len(arr)-1][x], move_item
    
    for y in range(len(arr)-2, machine_y, -1):
        move_item, arr[y][0] = arr[y][0], move_item
    move_item = None

def dust_count(arr):
    dust = 0
    for y in range(len(arr)):
        dust += sum(arr[y])
    return dust+2

if __name__ == "__main__":

    H, W, T = map(int, sys.stdin.readline().rstrip().split(' '))
    MAX_X, MAX_Y = W, H
    arr, machine_coord = [], []
    for y in range(H):
        temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        for x in range(len(temp)):
            if temp[x] == -1 :
                machine_coord.append((y, x))
        arr.append(temp)
    time = 0
    while time < 1000:
        if time == T : break
        arr = spread(arr)
        machine_work(arr)
        time += 1
    print(dust_count(arr))

