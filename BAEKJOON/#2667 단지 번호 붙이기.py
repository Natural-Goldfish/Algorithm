def makeArray(N, temp):
    visited = []
    array = []
    for i in range(len(temp)):
        visited.append([0]*len(temp))
        temp2 = []
        for j in range(len(temp[i])):
            temp2.append(temp[i][j])
        array.append(temp2)
    
    return visited, array

def solution(N, temp):
    visited, array = makeArray(N, temp)
    numbers = []
    for y in range(N):
        for x in range(N):
            if array[y][x] == 1 and visited[y][x] == 0:
                count = BFS(x, y, array, visited)
                numbers.append(count)
    
    numbers.sort()

    print(len(numbers))
    for i in range(len(numbers)):
        print(numbers[i])

def BFS(startX, startY, array, visited) :
    N = len(array)
    queue = [str(startX) + " " + str(startY)]
    count = 0
    while queue:
        curX, curY = map(int, queue.pop(0).split(" "))
        if visited[curY][curX] == 1 : continue

        visited[curY][curX] = 1
        count += 1

        # LEFT 
        if curX - 1 < 0 : pass
        else :
            if array[curY][curX - 1] == 1 and visited[curY][curX - 1] == 0 :
                queue.append(str(curX - 1) + " " + str(curY))
        # RIGHT
        if curX + 1 >= N : pass
        else :
            if array[curY][curX + 1] == 1 and visited[curY][curX + 1] == 0 :
                queue.append(str(curX + 1) + " " + str(curY))
        # UP
        if curY - 1 < 0 : pass
        else :
            if array[curY - 1][curX] == 1 and visited[curY - 1][curX] == 0 :
                queue.append(str(curX) + " " + str(curY - 1))
        # DOWN
        if curY + 1 >= N : pass
        else :
            if array[curY + 1][curX] == 1 and visited[curY + 1][curX] == 0 :
                queue.append(str(curX) + " " + str(curY + 1))
    return count

if __name__ == "__main__":
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(map(int, input())))
    
    solution(N, temp)