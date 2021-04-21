
global MIN_X, MIN_Y, MAX_Y, MAX_X, max_eaten_desserts
MIN_X, MIN_Y = 0, 0
def DFS(cur_coord, visited_coords, visited_dirs, eaten_desserts):
    global MIN_X, MIN_Y, MAX_Y, MAX_X, max_eaten_desserts
    y, x = cur_coord

    if not visited_coords and not visited_dirs and not eaten_desserts :
        pass    # 가장 처음
    else :
        if (y, x) in visited_coords and (y, x) == visited_coords[0] and len(visited_dirs) == 4:   # 현재 좌표가 가장 처음 방문한 좌표에 있는 경우
            max_eaten_desserts = max(len(eaten_desserts), max_eaten_desserts)
            return
        if (y, x) in visited_coords and (y, x) != visited_coords[0] : # 왔던길 또 온 경우
            return
        if arr[y][x] in eaten_desserts : 
            return

    # 우상 - 0
    dy, dx = -1, 1
    new_y, new_x = y + dy, x + dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        new_dessert = arr[new_y][new_x]

        if 0 not in visited_dirs :      #  처음 가는 방향
            visited_coords.append((y, x)), visited_dirs.append(0), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), visited_dirs.pop(), eaten_desserts.pop()
        elif visited_dirs[-1] == 0 :    # 계속 진행중인 경우
            visited_coords.append((y, x)), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), eaten_desserts.pop()
        else : pass # 다른 방향 갔다가 다시 가려는 경우
            

    # 우하 - 1
    dy, dx = 1, 1
    new_y, new_x = y + dy, x + dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        new_dessert = arr[new_y][new_x]
        if 1 not in visited_dirs :      #  처음 가는 방향
            visited_coords.append((y, x)), visited_dirs.append(1), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), visited_dirs.pop(), eaten_desserts.pop()
        elif visited_dirs[-1] == 1 :    # 계속 진행중인 경우
            visited_coords.append((y, x)), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), eaten_desserts.pop()
        else : pass # 다른 방향 갔다가 다시 가려는 경우    

    # 좌상 - 2
    dy, dx = -1, -1
    new_y, new_x = y + dy, x + dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        new_dessert = arr[new_y][new_x]
        if 2 not in visited_dirs :      #  처음 가는 방향
            visited_coords.append((y, x)), visited_dirs.append(2), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), visited_dirs.pop(), eaten_desserts.pop()
        elif visited_dirs[-1] == 2 :    # 계속 진행중인 경우
            visited_coords.append((y, x)), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), eaten_desserts.pop()
        else : pass # 다른 방향 갔다가 다시 가려는 경우    

    # 좌하 - 3
    dy, dx = 1, -1
    new_y, new_x = y + dy, x + dx
    if new_y < MIN_Y or new_y >= MAX_Y or new_x < MIN_X or new_x >= MAX_X : pass
    else :
        new_dessert = arr[new_y][new_x]
        if 3 not in visited_dirs :      #  처음 가는 방향
            visited_coords.append((y, x)), visited_dirs.append(3), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), visited_dirs.pop(), eaten_desserts.pop()
        elif visited_dirs[-1] == 3 :    # 계속 진행중인 경우
            visited_coords.append((y, x)), eaten_desserts.append(arr[y][x])
            DFS((new_y, new_x), visited_coords, visited_dirs, eaten_desserts)
            visited_coords.pop(), eaten_desserts.pop()
        else : pass # 다른 방향 갔다가 다시 가려는 경우
    

if __name__ == "__main__":
    T = int(input().rstrip())
    for test_case in range(1, T + 1):
        N = int(input().rstrip())
        arr = []
        for y in range(N):
            arr.append(list(map(int, input().rstrip().split(' '))))
        MAX_X, MAX_Y = len(arr[0]), len(arr)
        max_eaten_desserts = 0
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                DFS((y, x), [], [], [])
        if max_eaten_desserts == 0 : 
            max_eaten_desserts = -1
        
        print("#{} {}".format(test_case, max_eaten_desserts))