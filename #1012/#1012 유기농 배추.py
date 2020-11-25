
def makeArray(ArrayListInfo, ArrayListCoord):
    ArrayList = []
    VisitedList = []

    for i in range(len(ArrayListInfo)):
        M, N, K = ArrayListInfo[i]
        array = []
        visited = []

        for j in range(N):
            array.append([0]*M)
            visited.append([0]*M)

        for j in range(K):
            x, y = ArrayListCoord[i][j]
            array[y][x] = 1
    
        ArrayList.append(array)
        VisitedList.append(visited)

    return ArrayList, VisitedList

def solution(TestCase, ArrayList, VisitedList):
    for curTestCase in range(TestCase):
        array = ArrayList[curTestCase]
        visited = VisitedList[curTestCase]
        Area = 0

        for y in range(len(array)):
            for x in range(len(array[y])):
                if array[y][x] == 1 and visited[y][x] == 0 :
                    BFS((x, y), array, visited)
                    Area += 1
        
        print(Area)

def BFS(startPoint, array, visited):
    queue = [startPoint]

    while queue:
        x, y = queue.pop(0)
        if visited[y][x] == 1 : continue
        visited[y][x] = 1
        array[y][x] = 0
        # LEFT
        if x - 1 < 0 : pass
        else:
            if visited[y][x - 1] == 0 and array[y][x - 1] == 1:
                queue.append((x - 1, y))
        # RIGHT
        if x + 1 >= len(array[y]) : pass
        else :
            if visited[y][x + 1] == 0 and array[y][x + 1] == 1:
                queue.append((x + 1, y))
        # UP
        if y -1 < 0 : pass
        else :
            if visited[y - 1][x] == 0 and array[y - 1][x] == 1:
                queue.append((x, y - 1))
        # BOTTOM
        if y + 1 >= len(array) : pass
        else :
            if visited[y + 1][x] == 0 and array[y + 1][x] == 1:
                queue.append((x, y + 1))

    
if __name__ == "__main__":

    TestCase = int(input())

    ArrayList = []

    for i in range(TestCase):
        ArrayList.append([])
    
    ArrayListInfo = []
    ArrayListCoord = []
    for i in range(TestCase):
        M, N, K = map(int, input().split(" "))
        temp = []
        for j in range(K):
            x, y = map(int, input().split(" "))
            temp.append((x, y))
        ArrayListInfo.append([M, N, K])
        ArrayListCoord.append(temp)
    
    ArrayList, VisitedList = makeArray(ArrayListInfo, ArrayListCoord)
    solution(TestCase, ArrayList, VisitedList)