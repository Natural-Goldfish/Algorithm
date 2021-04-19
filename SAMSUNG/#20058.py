import copy, sys
from collections import deque

global ice_map
def fireStorm(skill_level):
    global ice_map
    loop_num = 2**skill_level       # if skill_level = 2, loop -> 4 번
    step = 2**skill_level         # if skill_level = 2, 한 변 길이가 4

    new_ice_map = [[0 for _ in range(len(ice_map))] for _ in range(len(ice_map))]
    for y in range(0, len(ice_map), step):
        for x in range(0, len(ice_map), step):
            section_length = step-1
            for y_in in range(step):
                for x_in in range(step):
                    new_ice_map[x_in+y][section_length-y_in+x] = ice_map[y+y_in][x+x_in]
    ice_map = new_ice_map
    new_ice_map = None

def damage():
    global ice_map
    MAX_X, MAX_Y = len(ice_map), len(ice_map)
    new_ice_map = copy.deepcopy(ice_map)
    for y in range(len(ice_map)):
        for x in range(len(ice_map)):
            if ice_map[y][x] == 0 : continue
            
            check = 0
            # UP
            dy, dx = -1, 0
            new_y, new_x = dy+y, dx+x
            if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
                pass
            else :
                if ice_map[new_y][new_x] != 0 :
                    check +=1
            # DOWN
            dy, dx = 1, 0
            new_y, new_x = dy+y, dx+x
            if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
                pass
            else :
                if ice_map[new_y][new_x] != 0 :
                    check +=1
            # LEFT
            dy, dx = 0, -1
            new_y, new_x = dy+y, dx+x
            if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
                pass
            else :
                if ice_map[new_y][new_x] != 0 :
                    check +=1
            # RIGHT
            dy, dx = 0, 1
            new_y, new_x = dy+y, dx+x
            if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
                pass
            else :
                if ice_map[new_y][new_x] != 0 :
                    check +=1                                                        

            if check < 3 :
                new_ice_map[y][x] -= 1
    ice_map = new_ice_map
    new_ice_map = None

def bfs(start_coord):
    global ice_map, visited
    MAX_X, MAX_Y = len(ice_map), len(ice_map)
    count = 0
    queue = deque([start_coord])
    while queue :
        y, x = queue.popleft()
        if ice_map[y][x] == 0 or visited[y][x] == True : continue
        
        visited[y][x] = True
        count += 1

        # UP
        dy, dx = -1, 0
        new_y, new_x = dy+y, dx+x
        if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
            pass
        else :
            if ice_map[new_y][new_x] != 0 :
                queue.append((new_y, new_x))
        # DOWN
        dy, dx = 1, 0
        new_y, new_x = dy+y, dx+x
        if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
            pass
        else :
            if ice_map[new_y][new_x] != 0 :
                queue.append((new_y, new_x))
        # LEFT
        dy, dx = 0, -1
        new_y, new_x = dy+y, dx+x
        if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
            pass
        else :
            if ice_map[new_y][new_x] != 0 :
                queue.append((new_y, new_x))
        # RIGHT
        dy, dx = 0, 1
        new_y, new_x = dy+y, dx+x
        if new_x<0 or new_x>=MAX_X or new_y <0 or new_y >=MAX_Y :
            pass
        else :
            if ice_map[new_y][new_x] != 0 :
                queue.append((new_y, new_x)) 

    if count == 1 :
        return 0
    return count

if __name__ == "__main__":
    N, Q = map(int, sys.stdin.readline().rstrip().split(' '))
    ice_map, visited = [], []

    for y in range(2**N):
        ice_map.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
        visited.append([False for _ in range(2**N)])

    skill_level_list= list(map(int, sys.stdin.readline().rstrip().split(' ')))
    
    for skill_level in skill_level_list:
        fireStorm(skill_level)
        damage()
    summary = 0
    big_ice = 0
    for y in range(2**N):
        summary += sum(list(filter(lambda x : x !=0, ice_map[y])))
        for x in range(2**N):
            big_ice = max(big_ice, bfs((y, x)))
        
    print(summary)
    print(big_ice)
