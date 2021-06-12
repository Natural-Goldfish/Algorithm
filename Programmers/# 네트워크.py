def BFS(startNode, computers, visited):
    if visited[startNode] == 1 : 
        return False

    queue = [startNode]
    
    while queue :
        curNode = queue.pop(0)
        visited[curNode] = 1
        
        toVisit = computers[curNode]
        
        for i in range(len(toVisit)):
            if toVisit[i] == 1 and visited[i] == 0 and i not in queue :
                queue.append(i)
        
    return True

def solution(n, computers):
    visited = [0]*n
    count = 0
        
    for y in range(len(computers)):
        for x in range(len(computers[y])):
            if computers[y][x] == 1 :
                temp = BFS(y, computers, visited)
                if temp : count += 1
    
    answer = count
    return answer