def BFS(startPoint, array, visited, width, height):
    x, y = startPoint
    if array[y][x] == 0 or visited[y][x] == 1: return False

    queue = [startPoint]

    while(queue):
        x, y = queue.pop(0)
        if visited[y][x] == 1 : continue
        visited[y][x] = 1
        
        # LEFT
        if x - 1 < 0 : pass
        else :
            if array[y][x - 1] == 1 and visited[y][x - 1] == 0 and (x - 1, y) not in queue :
                queue.append((x - 1, y))
        # LEFT UP
        if x - 1 < 0 or y - 1 < 0 : pass
        else :
            if array[y - 1][x - 1] == 1 and visited[y - 1][x - 1] == 0 and (x - 1, y - 1) not in queue :
                queue.append((x - 1, y - 1))
        # LEFT DOWN
        if x - 1 < 0 or y + 1 >= height : pass
        else :
            if array[y + 1][x - 1] == 1 and visited[y + 1][x - 1] == 0 and (x - 1, y + 1) not in queue :
                queue.append((x - 1, y + 1))
        # RIGHT
        if x + 1 >= width : pass
        else :
            if array[y][x + 1] == 1 and visited[y][x + 1] == 0 and (x + 1, y) not in queue :
                queue.append((x + 1, y))
        # RIGHT UP
        if x + 1 >= width or y - 1 < 0 : pass
        else :
            if array[y - 1][x + 1] == 1 and visited[y - 1][x + 1] == 0 and (x + 1, y - 1) not in queue :
                queue.append((x + 1, y - 1))
        # RIGHT DOWN
        if x + 1 >= width or y + 1 >= height : pass
        else :
            if array[y + 1][x + 1] == 1 and visited[y + 1][x + 1] == 0 and (x + 1, y + 1) not in queue :
                queue.append((x + 1, y + 1))
        # UP
        if y - 1 < 0 : pass 
        else :
            if array[y - 1][x] == 1 and visited[y - 1][x] == 0 and (x, y - 1) not in queue :
                queue.append((x, y - 1))
        # DOWN
        if y + 1 >= height : pass
        else :
            if array[y + 1][x] == 1 and visited[y + 1][x] == 0 and (x, y + 1) not in queue :
                queue.append((x, y + 1))
    return True
if __name__ == "__main__":
    width = -1
    height = -1
    while(width != 0 and height != 0):
        width, height = map(int, input().split(" "))
        if width == 0 and height == 0 : 
            break
        array = []
        visited = []
        count = 0
        for i in range(height):
            array.append(list(map(int, input().split(" "))))
            visited.append([0]*width)
        
        for y in range(height):
            for x in range(width):
                flag = BFS((x, y), array, visited, width, height)
                if flag : count += 1
                else : pass
        print(count)
        