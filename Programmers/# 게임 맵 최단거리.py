from collections import deque

def bfs(start_point, arr):
    queue, visited = deque([(0, 0)]), set()
    min_num = 0
    while queue :
        queue2 = deque([])
        while queue :
            y, x = queue.popleft()
            if (y, x) in visited : continue
            visited.add((y, x))
            
            # RIGHT
            dy, dx = 0, 1
            new_y, new_x = y+dy, x+dx
            if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]) :
                pass
            else :
                if arr[new_y][new_x] != 0 :
                    queue2.append((new_y, new_x))
            # LEFT
            dy, dx = 0, -1
            new_y, new_x = y+dy, x+dx
            if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]) :
                pass
            else :
                if arr[new_y][new_x] != 0 :
                    queue2.append((new_y, new_x))
            # UP
            dy, dx = -1, 0
            new_y, new_x = y+dy, x+dx            
            if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]) :
                pass
            else :
                if arr[new_y][new_x] != 0 :
                    queue2.append((new_y, new_x))
            # DOWN
            dy, dx = 1, 0
            new_y, new_x = y+dy, x+dx            
            if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]) :
                pass
            else :
                if arr[new_y][new_x] != 0 :
                    queue2.append((new_y, new_x))
        if (len(arr)-1, len(arr[0])-1) in visited :
            return min_num+1
        queue = queue2
        min_num += 1
    return -1
def solution(maps):
    return bfs((0, 0), maps)
