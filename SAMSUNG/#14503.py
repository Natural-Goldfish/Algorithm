global DIRECTION, MAX_ROTATE_NUM, CUR_DIRECTION
DIRECTION = {
    0 : (-1, 0),      # 북
    1 : (0, -1),      # 서
    2 : (1, 0),       # 남
    3 : (0, 1)        # 동
}

MAX_ROTATE_NUM = 4
CUR_DIRECTION = -1

def converter(direction):
    # 0 1 2 3 북 동 남 서
    global CUR_DIRECTION
    
    if direction == 0 : 
        CUR_DIRECTION = 0
    elif direction == 1 :
        CUR_DIRECTION = 3
    elif direction == 2 :
        CUR_DIRECTION = 2
    else :
        CUR_DIRECTION = 1


def search(cur_coord, arr): # return next coord
    global MAX_ROTATE_NUM, CUR_DIRECTION
    y, x = cur_coord
    for i in range(MAX_ROTATE_NUM):
        next_direction = (CUR_DIRECTION + 1) % MAX_ROTATE_NUM
        dy, dx = DIRECTION[next_direction]
        if arr[y+dy][x+dx] == 0 :
            CUR_DIRECTION = next_direction
            return (1, y+dy, x+dx)
        CUR_DIRECTION = next_direction

    if CUR_DIRECTION % 4 == 0 :
        CUR_DIRECTION = 0

    next_direction = (CUR_DIRECTION+2) % MAX_ROTATE_NUM
    dy, dx = DIRECTION[next_direction]
    if arr[y+dy][x+dx] == 1 :
        return (-1, -1, -1)
    else :
        return (0, y+dy, x+dx)


if __name__ == "__main__":
    H, W = map(int, input().rstrip().split(' '))
    y, x, direction = map(int, input().rstrip().split(' '))
    converter(direction)
    cur_coord = (y, x)

    arr = []
    for h in range(H):
        arr.append(list(map(int, input().rstrip().split(' '))))

    count = 0 
    not_finish = True
    while not_finish :
        y, x = cur_coord
        arr[y][x] = -1
        count += 1
        while True :
            flag, new_y, new_x= search((y, x), arr)
            cur_coord = (new_y, new_x)
            if flag == 1 :
                break
            elif flag == 0 :
                if arr[new_y][new_x] == -1 :
                    count -= 1
                break
            elif flag == -1 :
                not_finish = False
                break

    print(count)

    """
    1 1 1 1 1 1 1 1 1 1
    1 0 0 0 0 0 0 0 0 1
    1 0 0 0 1 1 1 1 0 1
    1 0 0 1 1 0 0 0 0 1
    1 0 1 1 -6 -5 0 0 0 1
    1 0 0 -8 -7 -4 -3 0 0 1
    1 0 -10 -9 -1 -2 0 1 -30 1
    1 -17 -11 -12 -15 -16 1 1 -29 1
    1 -18 -19 -22 -13 -14 1 1 -28 1
    1 0 -20 -21 -23 -24 -25 -26 -27 1
    1 1 1 1 1 1 1 1 1 1
    """