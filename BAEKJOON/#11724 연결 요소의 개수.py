import sys

def BFS(startNode, array, visited):
    queue = [startNode]

    if visited[startNode] == 1 :
        return False

    while queue : 
        curNode = queue.pop(0)
        if visited[curNode] == 1 : continue
        visited[curNode] = 1
        toVisit = array[curNode]
        for i in toVisit:
            if visited[i] == 0 and i not in queue :
                queue.append(i)

    return True
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    number = 0
    array = []
    visited = [0]*(N)

    for i in range(N):
        array.append([])

    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        array[x - 1].append(y - 1)
        array[y - 1].append(x - 1)
        
    for i in range(len(array)):
        if visited[i] == 0 :
            temp = BFS(i, array, visited)
            if temp == False : pass
            elif temp == True : number += 1
    print(number)