def solution(array, visited):
    AreaList = []
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] != -1 :
                temp = BFS((x, y), array, visited)
                if temp != -1 : AreaList.append(temp)
    if len(AreaList) == 0 :
        print(0)
    else :
        print(len(AreaList))
        AreaList.sort()
        for i in range(len(AreaList)):
            print(AreaList[i], end = " ")

def arrayInit(array, pointList):
    for i in range(len(pointList)):
        Lx, Ly, Rx, Ry = pointList.pop(0)
        for y in range(Ly, Ry):
            for x in range(Lx, Rx):
                array[y][x] = -1

def BFS(startPoint, array, visited):
    x, y = startPoint
    if visited[y][x] == 1 : return -1
    queue = [startPoint]
    count = 0
    while queue :
        x, y = queue.pop(0)
        visited[y][x] = 1

        # LEFT
        if x - 1 < 0 : pass
        else :
            if visited[y][x - 1] == 0 and array[y][x - 1] != -1 and (x - 1, y) not in queue :
                queue.append((x - 1, y))
        # RIGHT
        if x + 1 >= len(array[y]) : pass
        else :
            if visited[y][x + 1] == 0 and array[y][x + 1] != -1 and (x + 1, y) not in queue :
                queue.append((x + 1, y))
        # UP
        if y - 1 < 0 : pass
        else :
            if visited[y - 1][x] == 0 and array[y - 1][x] != -1 and (x, y - 1) not in queue :
                queue.append((x, y - 1))
        # DOWN
        if y + 1 >= len(array) : pass
        else :
            if visited[y + 1][x] == 0 and array[y + 1][x] != -1 and (x, y + 1) not in queue :
                queue.append((x, y + 1))
        count += 1

    return count
if __name__ == "__main__":
    M, N, K = map(int, input().split(" "))

    array = []
    visited = []

    for i in range(M):
        array.append([0]*N)
        visited.append([0]*N)
    
    pointList = []

    for i in range(K):
        Lx, Ly, Rx, Ry = map(int, input().split(" "))
        pointList.append((Lx, len(array) - Ry, Rx, len(array) - Ly))

    arrayInit(array, pointList)
    solution(array, visited)