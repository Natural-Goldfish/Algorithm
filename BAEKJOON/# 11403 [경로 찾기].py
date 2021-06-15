import sys, copy
from collections import deque

N = int(str.rstrip(sys.stdin.readline(), ''))
graph = [list(map(int, str.rstrip(sys.stdin.readline(), '').split(' '))) for _ in range(N)]
answer = copy.deepcopy(graph)

def bfs(start, answer):
    queue = deque([start])
    visited = set()
    while queue :
        i = queue.popleft()
        if i in visited : continue
        visited.add(i)
        for index, node in enumerate(graph[i]):
            if node == 1:
                queue.append(index)
                answer[start][index] = 1
for index in range(N):
    bfs(index, answer)   
for index in range(N):
    print(' '.join(map(str, answer[index])))