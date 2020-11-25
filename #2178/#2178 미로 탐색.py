def makeArray(Maze):
    newMaze = []
    visited = []
    for y in range(len(Maze)):
        temp = []
        for x in range(len(Maze[i])):
            temp.append(int(Maze[y][x]))
        newMaze.append(temp)
        visited.append([0]*(x+1))
    return visited, newMaze

def solution(N, M, Maze):
    visited, Maze = makeArray(Maze)
    BFS(M-1, N-1, visited, Maze)

def BFS(startX, startY, visited, Maze):
    queue = [str(startX) + " " + str(startY)]
    queueCount = [0]
    countList = []
    count = 0

    while queue :
        curX, curY = map(int, queue.pop(0).split(" "))
        count = queueCount.pop(0)

        if visited[curY][curX] != 0 :
            continue

        # FIND
        if curX == 0 and curY == 0 :
            print(count + 1)
            break

        visited[curY][curX] = count + 1

        # LEFT
        if curX - 1 < 0 : pass
        else :
            if Maze[curY][curX - 1] == 1 and visited[curY][curX - 1] == 0 :
                queueCount.append(visited[curY][curX])
                queue.append(str(curX - 1) + " " + str(curY))
        # RIGHT
        if curX + 1 >= startX + 1 : pass
        else:
            if Maze[curY][curX + 1] == 1 and visited[curY][curX + 1] == 0 :
                queueCount.append(visited[curY][curX])
                queue.append(str(curX + 1) + " " + str(curY))                   
        # UP
        if curY - 1 < 0 : pass
        else :
            if Maze[curY - 1][curX] == 1 and visited[curY - 1][curX] == 0 :
                queueCount.append(visited[curY][curX])
                queue.append(str(curX) + " " + str(curY - 1))
        # DOWN
        if curY + 1 >= startY + 1 : pass
        else:
            if Maze[curY + 1][curX] == 1 and visited[curY + 1][curX] == 0 :
                queueCount.append(visited[curY][curX])
                queue.append(str(curX) + " " + str(curY + 1))

if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    Maze = []
    for i in range(N):
        Maze.append(input())

    solution(N, M, Maze)