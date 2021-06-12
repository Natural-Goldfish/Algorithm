def solution(M, N, array, visited):
    flag = False
    day = 0
    tomatoList = modifyVisited(array, visited)

    if len(tomatoList) == 0 : print(-1)
    else :
        while tomatoList :
            tempArray = []
            for i in range(len(tomatoList)):
                x, y = tomatoList[i]
                if visited[y][x] == 0 and array[y][x] == 1:
                    temp = search(x, y, array, visited)
                    if temp == None : pass
                    else : tempArray.extend(temp)
            tomatoList = tempArray
            if len(tomatoList) == 0 : break
            else : day += 1

        for i in range(len(array)):
            if 0 in array[i] : 
                flag = True
                
        if flag : print(-1)
        else : print(day)

def modifyVisited(array, visited):
    tomatoList = []
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 1 : tomatoList.append((x, y))
    return tomatoList

def search(x, y, array, visited):
    temp = []
    array[y][x] = 2
    visited[y][x] = 1

    # LEFT
    if x - 1 < 0 : pass
    else :
        if array[y][x - 1] == 0 : 
            temp.append((x - 1, y))
            array[y][x - 1] = 1

    # RIGHT
    if x + 1 >= len(array[y]) : pass
    else :
        if array[y][x + 1] == 0 : 
            temp.append((x + 1, y))
            array[y][x + 1] = 1
    
    # UP
    if y + 1 >= len(array) : pass
    else :
        if array[y + 1][x] == 0 : 
            temp.append((x, y + 1))
            array[y + 1][x] = 1

    # BOTTOM
    if y - 1 < 0 : pass
    else :
        if array[y - 1][x] == 0 : 
            temp.append((x, y - 1))
            array[y - 1][x] = 1

    if len(temp) == 0 :
        return None
    else :
        return temp

if __name__=="__main__":
    M, N = map(int, input().split(" "))
    array = []
    visited = []
    for i in range(N):
        array.append(list(map(int, input().split(" "))))
        visited.append([0]*M)
    solution(M, N, array, visited)
    