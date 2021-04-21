import copy

global MIN_X, MIN_Y, MAX_X, MAX_Y, carr, max_length, visited
MIN_X, MIN_Y = 0, 0



def process(arr, origin_max_coord):
    global carr, visited
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            for k in range(0, K+1):
                if arr[y][x] - k < 0 : continue
                
                carr = copy.deepcopy(arr)
                carr[y][x] = carr[y][x] - k

                cur_highest_coord = origin_max_coord - set([(y, x)])
                if not cur_highest_coord :
                    cur_highest_coord = find_highest(carr)
                
                for cur_coord in cur_highest_coord :
                    visited = set()
                    dfs(cur_coord, 0)

def dfs(cur_coord, length):
    global MIN_X, MIN_Y, MAX_X, MAX_Y, max_length, visited
    y, x = cur_coord
    cur_height = carr[y][x]

    length += 1
    visited.add((y, x))

    # up
    dy, dx = -1, 0
    new_y, new_x = y+dy, x+dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        if carr[new_y][new_x] < cur_height and (new_y, new_x) not in visited:
            dfs((new_y, new_x), length)
        else :
            pass
    # down
    dy, dx = 1, 0
    new_y, new_x = y+dy, x+dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        if carr[new_y][new_x] < cur_height and (new_y, new_x) not in visited :
            dfs((new_y, new_x), length)
        else :
            pass
    # left
    dy, dx = 0, -1
    new_y, new_x = y+dy, x+dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        if carr[new_y][new_x] < cur_height and (new_y, new_x) not in visited :
            dfs((new_y, new_x), length)
        else :
            pass
    # right
    dy, dx = 0, 1
    new_y, new_x = y+dy, x+dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        if carr[new_y][new_x] < cur_height and (new_y, new_x) not in visited :
            dfs((new_y, new_x), length)
        else :
            pass
    
    visited = visited - set([(y, x)])
    max_length = max(max_length, length)

def find_highest(arr):
    max_row = []
    for y in range(len(arr)):
        max_row.append(max(arr[y]))
    max_height = max(max_row)

    max_coord = []
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == max_height :
                max_coord.append((y, x))
    return max_coord

if __name__ == '__main__':
    T = int(input().rstrip())
    for test_case in range(1, T + 1):
        N, K = map(int, input().rstrip().split(' '))
        MAX_X, MAX_Y = N, N
        max_length = 0
        arr = []
        carr, visited  = [], []
        for y in range(N):
            arr.append(list(map(int, input().rstrip().split(' '))))
        origin_max_coord = set(find_highest(arr))

        process(arr, origin_max_coord)
        print("#{} {}".format(test_case, max_length))