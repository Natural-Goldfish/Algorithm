from itertools import product
from collections import deque
import copy

global MIN_X, MIN_Y, MAX_X, MAX_Y

def bfs(index_x, graph, count):
    y, x= getCoord(index_x, graph)
    if y == -1 or x == - 1 :
        return 0
    queue = deque([(y, x)])
    while queue :
        y, x = queue.popleft()
        if graph[y][x] == 0 : continue
        distance = graph[y][x]-1
        graph[y][x] = 0
        count += 1
        if distance == 0 : continue

        for increase in range(1, distance+1):
            if y+increase < MIN_Y or y+increase >= MAX_Y : pass
            elif graph[y+increase][x] != 0 :
                queue.append((y+increase, x))
            if x+increase < MIN_X or x+increase >= MAX_X : continue
            elif graph[y][x+increase] != 0 :
                queue.append((y, x+increase))
        for decrease in range(-1, -distance-1, -1):
            if y+decrease < MIN_Y or y+decrease >= MAX_Y : pass
            elif graph[y+decrease][x] != 0 :
                queue.append((y+decrease, x))
                
            if x+decrease < MIN_X or x+decrease >= MAX_X : continue
            elif graph[y][x+decrease] != 0 :
                queue.append((y, x+decrease))
    return count

def createGraph(graph):
    new_graph = [[0 for j in range(len(graph[0]))] for i in range(len(graph))]
    for x in range(len(graph[0])):
        index = len(graph)-1
        for y in range(len(graph)-1, -1, -1):
            if graph[y][x] != 0 :
                new_graph[index][x] = graph[y][x]
                index -= 1
    return new_graph

def getCoord(index_x, graph) -> (int, int):
    for index_y, temp_list in enumerate(graph):
        if temp_list[index_x] != 0 :
            return (index_y, index_x)
    return (-1, -1)

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        N, W, H = map(int, input().rstrip().split(' '))
        MIN_X, MIN_Y, MAX_X, MAX_Y = 0, 0, W, H
        graph = []
        scores = 0
        for i in range(MAX_Y):
            graph.append(list(map(int, input().rstrip().split(' '))))

        available_case = list(product([i for i in range(W)], repeat=N))
        for case in available_case:
            temp_graph = copy.deepcopy(graph)
            count = 0
            for index_x in case :
                count = bfs(index_x, temp_graph, count)
                temp_graph = createGraph(temp_graph)
            if count :
                scores = max(count, scores)
        another_score = 0                
        if scores != 0 :    
            for y in range(len(graph)):
                for x in range(len(graph[0])):
                    if graph[y][x] != 0 :
                        another_score += 1       
        print("#{} {}".format(test_case, another_score - scores))