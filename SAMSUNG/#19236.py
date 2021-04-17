import copy
global N, SCORE, DIRECTION, MIN_X, MIN_Y, MAX_X, MAX_Y
MIN_X, MIN_Y, MAX_X, MAX_Y = 0, 0, 4, 4
N, SCORE = 4, 0
DIRECTION = {
    1 : (-1, 0),        # 상
    2 : (-1, -1),       # 좌상
    3 : (0, -1),        # 좌
    4 : (1, -1),        # 좌하
    5 : (1, 0),         # 하
    6 : (1, 1),         # 우하
    7 : (0, 1),         # 우
    8 : (-1, 1),        # 우상
}

def DFS(startXY, arr, score):
    global SCORE
    y, x = startXY
    fishNum, direction = arr[y][x]                      
    if fishNum == 0 or direction == 0: return       # No fish
    arr[y][x] = (-1, -1)                            # Baby shark

    score = fishNum + score
    SCORE = max(score, SCORE)
    
    # fish move
    fishMove(arr)
    arr[y][x] = (0, 0)
    for i in range(1, N+1):
        dy, dx = DIRECTION[direction][0]*i, DIRECTION[direction][1]*i
        if x + dx < MIN_X or x + dx >= MAX_X or y + dy < MIN_Y or y + dy >= MAX_Y : break
        DFS((y + dy, x + dx), copy.deepcopy(arr), score)
    
    
def fishMove(arr):
    temp = {i+1 : [] for i in range(0, N*N)}                
    for y in range(N):
        for x in range(N):
            if arr[y][x] != (-1, -1) and arr[y][x] != (0, 0):
                temp[arr[y][x][0]] = (arr[y][x][1], y, x)

    for fishNum in range(1, N*N+1):
        if not temp[fishNum] : continue
        for i in range(8):
            direction, y, x = temp[fishNum]
            dy, dx  = DIRECTION[direction][0], DIRECTION[direction][1]
            if x + dx < MIN_X or x + dx >= MAX_X or y + dy < MIN_Y or y + dy >= MAX_Y :
                temp[fishNum] = (temp[fishNum][0] + 1, temp[fishNum][1], temp[fishNum][2])
                if temp[fishNum][0] > 8 :
                    temp[fishNum] = (1, temp[fishNum][1], temp[fishNum][2])
                continue
            elif arr[y + dy][x + dx] == (-1, -1) : 
                temp[fishNum] = (temp[fishNum][0] + 1, temp[fishNum][1], temp[fishNum][2])
                if temp[fishNum][0] > 8 :
                    temp[fishNum] = (1, temp[fishNum][1], temp[fishNum][2])
                continue
            else :
                new_y, new_x = y+dy, x+dx
                if arr[new_y][new_x] == (0, 0):
                    temp[fishNum] = (temp[fishNum][0], new_y, new_x)
                    arr[new_y][new_x] = (fishNum, temp[fishNum][0])
                    arr[y][x] = (0, 0)
                else :
                    temp[fishNum], temp[arr[new_y][new_x][0]] = (temp[fishNum][0], new_y, new_x), (temp[arr[new_y][new_x][0]][0], y, x)
                    arr[new_y][new_x], arr[y][x] = (fishNum, temp[fishNum][0]), (arr[new_y][new_x][0], temp[arr[new_y][new_x][0]][0])
                break      


if __name__ == "__main__":
    arr = [[(0, 0) for i in range(N)] for j in range(N)]
    for i in range(N):
        temp = input().rstrip().split(" ")
        for index in range(0, len(temp), 2):
            arr[i][index//2] = (int(temp[index]), int(temp[index + 1]))         # fish number, diriection = (int, int) tuple
    DFS((0, 0), arr, 0)
    print(SCORE)