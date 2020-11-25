import copy

def DFS(curNode, visited, array):
    visited[curNode] = 1
    toVisit = array[curNode]
    print(curNode + 1, end = " ")
    for i in range(len(toVisit)):
        if toVisit[i] == 1 and visited[i] == 0:
            DFS(i, visited, array)
    return visited

def BFS(curNode, queue, visited, array):
    queue.append(curNode)

    while queue :
        curNode = queue.pop(0)
        if visited[curNode] == 1: continue

        print(curNode + 1, end = " ")
        visited[curNode] = 1
        toVisit = array[curNode]
        for i in range(len(toVisit)):
            if toVisit[i] == 1 and visited[i] == 0:
                queue.append(i)
    return visited

def makeArray(N):
    returnArray = []
    visited = [0]*N
    for i in range(N):
        temp = [0]*N
        returnArray.append(temp)
    return visited, returnArray

def markArray(array, connectionList):
    for i in range(len(connectionList)):
        array[connectionList[i][0] - 1][connectionList[i][1] - 1] = 1
        array[connectionList[i][1] - 1][connectionList[i][0] - 1] = 1

def solution(N, M, V, connectionList):
    visited, array = makeArray(N)
    markArray(array, connectionList)

    DFSList = DFS(V-1, copy.deepcopy(visited), copy.deepcopy(array))
    print()
    BFSList = BFS(V-1, [], copy.deepcopy(visited), copy.deepcopy(array))

if __name__ == "__main__":
    N, M, V = input().split(" ")
    N, M, V = int(N), int(M), int(V)
    connectionList = []
    for i in range(M):
        a, b = input().split(" ")
        a, b = int(a), int(b)
        connectionList.append([a, b])
    solution(N, M, V, connectionList)


