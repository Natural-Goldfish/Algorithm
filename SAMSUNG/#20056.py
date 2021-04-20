import sys

global MAX_X, MAX_Y, MIN_X, MIN_Y, arr, fireball_coord

DIRECTION = {
    0 : (-1, -1),
    1 : (-1, 1),
    2 : (0, 1),
    3 : (1, 1),
    4 : (1, 0),
    5 : (1, -1),
    6 : (0, -1),
    7 : (-1, -1),
}

def fireball_move():
    global fireball_coord, MIN_X, MIN_Y, MAX_X, MAX_Y, arr

    new_fireball_coord = []
    new_arr = [[[] for _ in range(MAX_Y)] for _ in range(MAX_X)]
    while fireball_coord :
        y, x = fireball_coord.pop()

        if not arr[y][x] :continue

        for coord in arr[y][x] :
            m, s, d = coord
            dy, dx= DIRECTION[d][0]*s, DIRECTION[d][1]*s
            new_y, new_x = dy+y, dx+x

            if new_x < MIN_X or new_x >= MAX_X or new_y < MIN_Y or new_y >= MAX_Y :
                if new_x < 0 :
                    new_x = MAX_X - abs(new_x)%MAX_X - 1
                elif new_x >= MAX_X:
                    new_x = abs(new_x)%MAX_X - 1
                if new_y < 0 :
                    new_Y = MAX_Y - abs(new_y)%MAX_Y - 1
                elif new_y >= MAX_Y :                
                    new_y = abs(new_y)%MAX_Y - 1
                if x !=0 and x!= MAX_X-1 and y!=0 and y != MAX_Y :
                    continue
            new_arr[new_y][new_x].append((m, s, d))
    
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if not new_arr[y][x] : continue
            else :
                if len(new_arr[y][x]) == 1 :
                    new_fireball_coord.append((y, x))
                    continue
                temp_list = new_arr[y][x]
                new_arr[y][x] = []
                flag_list = [False for _ in range(len(temp_list))]
                mm, ss = 0, 0
                for index, item in enumerate(temp_list) :
                    m, s, d = item
                    mm, ss = mm + m, ss + s
                    if d % 2 == 0 :
                        flag_list[index] = True
                
                # 조건 2
                mm, ss = int(mm/5), int(ss/len(temp_list))
                if mm == 0 : continue

                # 조건 3
                length = len(list(filter(lambda x : x, flag_list)))
                if length == 0 or length == len(temp_list) :
                    for d in [0, 2, 4, 6]:
                        new_arr[y][x].append((mm, ss, d))
                else :
                    for d in [1, 3, 5, 7]:
                        new_arr[y][x].append((mm, ss, d))
                
                new_fireball_coord.append((y, x))
    arr = new_arr
    new_arr = None
    fireball_coord = new_fireball_coord
    new_fireball_coord = None

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))
    N += 1
    MIN_X, MIN_Y, MAX_X, MAX_Y = 0, 0, N, N
    fireball_init = {}
    fireball_coord = []
    for i in range(M):
        y, x, m, s, d = map(int, sys.stdin.readline().rstrip().split(' '))
        fireball_init[(y-1, x-1)] = (m, s, d)
        fireball_coord.append((y-1, x-1))
    
    arr = [[ [] for _ in range(MAX_Y)] for _ in range(MAX_X)]
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if (y, x) in fireball_init :
                arr[y][x].append(fireball_init[(y, x)])
    for k in range(K):
        fireball_move()
    answer = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if not arr[y][x] : continue
            else :
                for item in arr[y][x] :
                    m, s, d = item
                    answer += m
    print(answer)

