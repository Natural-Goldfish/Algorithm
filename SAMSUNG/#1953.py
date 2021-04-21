from collections import deque
DIRECTION = {
    1 : [(-1, 0), (1, 0), (0, -1), (0, 1)], # 상 하 좌 우
    2 : [(-1, 0), (1, 0)],  # 상 하
    3 : [(0, -1), (0, 1)],  # 좌 우
    4 : [(-1, 0), (0, 1)],  # 상 우
    5 : [(1, 0), (0, 1)],   # 하 우
    6 : [(1, 0), (0, -1)],  # 하 좌
    7 : [(-1, 0), (0, -1)]  # 상 좌
}
global count 
count = 0

def BFS(start_coord, limit_time):
    global count, arr
    visited = set([])    
    queue = deque([start_coord])
    time = 1
    while time <= limit_time :
        next_queue = []
        while queue :
            y, x = queue.popleft()
            if (y, x) in visited :
                continue
            visited.add((y, x))
            count += 1
            d_list = arr[y][x]
            
            for dy, dx in d_list :
                new_y, new_x = dy+y, dx+x
                if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]) :
                    continue
                if (new_y, new_x) not in visited and check((dy, dx), arr[new_y][new_x]):
                    next_queue.append((new_y, new_x))
        queue = deque(next_queue)
        time += 1
    return len(visited)

def check(d1, d_list):
    y1, x1 = d1
    if y1 == 1 :
        y1 = -1
    elif y1 == -1 :
        y1 = 1
    if x1 == 1 :
        x1 = -1
    elif x1 == -1 :
        x1 = 1
    if (y1, x1) in d_list :
        return True
    else : return False
if __name__ == "__main__":
    T = int(input().rstrip());
    for test_case in range(1, T + 1):
        H, W, init_y, init_x, L = map(int, input().rstrip().split(' '))

        arr = [ [ [] for _ in range(W)] for _ in range(H)]
        for y in range(H):
            temp_list = list(map(int, input().rstrip().split(' ')))
            for x in range(len(temp_list)):
                if temp_list[x] != 0 :
                    arr[y][x] = DIRECTION[temp_list[x]]
        
        
        print("#{} {}".format(test_case, BFS((init_y, init_x), L)))