import copy

def solution(array):
    N = len(array)
    rainNumMax = max(max(array))
    rainNum = 0
    AreaList = []
    
    while(rainNum != rainNumMax + 1):
        curArray = arrayInit(copy.deepcopy(array), rainNum)
        visited = visitedInit(N)
        count = 0

        for y in range(len(curArray)):
            for x in range(len(curArray[y])):
                if curArray[y][x] != -1 :
                    flag = BFS((x, y), curArray, visited)
                    if flag : count += 1
        rainNum += 1
        AreaList.append(count)
    print(max(AreaList))

def BFS(startPoint, array, visited):
    x, y = startPoint
    if visited[y][x] == 1 : return False

    queue = [startPoint]

    while(queue):
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
        # BOTTOM 
        if y + 1 >= len(array): pass
        else :
            if visited[y + 1][x] == 0 and array[y + 1][x] != -1 and (x, y + 1) not in queue :
                queue.append((x, y + 1))

    return True

def visitedInit(N):
    temp = []
    for i in range(N):
        temp.append([0]*N)
    return temp

def arrayInit(array, rainNum):
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] <= rainNum : array[y][x] = -1
    return array

if __name__ == "__main__":
    N = int(input())
    array = []

    for i in range(N):
        array.append(list(map(int, input().split(" "))))
    
    solution(array)