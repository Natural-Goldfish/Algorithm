import sys
sys.setrecursionlimit(3000)
H, W = map(int, str.rstrip(sys.stdin.readline()).split(' '))
arr, path_arr, path = [], [], 0
for h in range(H):
    arr.append(list(map(int, str.rstrip(sys.stdin.readline()).split(' '))))
    path_arr.append([-1 for _ in range(W)])

def DFS(cur_coord, visited):
    y, x = cur_coord

    if y == 0 and x == 0 :
        return 1
    if path_arr[y][x] == -1 :
        path_arr[y][x] = 0

        # UP LEFT, RIGHT, DOWN
        dx, dy= [0, -1, 1, 0], [-1, 0, 0, 1]
        for index in range(4):
            new_x, new_y = x+dx[index], y+dy[index]
            if new_x < 0 or new_x >= W or new_y < 0 or new_y >= H : pass
            else :
                if arr[new_y][new_x] > arr[y][x] :
                    visited.add((new_y, new_x))
                    path_arr[y][x] += DFS((new_y, new_x), visited)
                    visited.remove((new_y, new_x))
    return path_arr[y][x]

print(DFS((H-1, W-1), set([(H-1, W-1)])))