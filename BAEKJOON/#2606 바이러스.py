def solution(array, visited):
    BFS(0, array, visited)

def BFS(startPoint, array, visited):
    queue = [startPoint]
    count = -1
    while queue :
        curNode = queue.pop(0)
        if visited[curNode] == 1 : continue
        visited[curNode] = 1
        count += 1
        toVisit = array[curNode]
        for i in range(len(toVisit)):
            if toVisit[i] == 1 and visited[i] == 0 :
                queue.append(i)
    print(count)

if __name__ == "__main__":
    N = int(input())
    array = []
    visited = [0]*N

    for i in range(N):
        array.append([0]*N)

    K = int(input())

    for i in range(K):
        fromPoint, toPoint = map(int, input().split(" "))
        array[fromPoint - 1][toPoint - 1] = 1
        array[toPoint - 1][fromPoint - 1] = 1

    solution(array, visited)
