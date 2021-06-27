import sys
from collections import deque

TEST_CASE = int(str.rstrip(sys.stdin.readline()))
answer_list = []
for test_case in range(1, TEST_CASE+1):
    N = int(str.rstrip(sys.stdin.readline()))
    arr = list(list(0 for _ in range(N)) for _ in range(N))
    cx, cy = map(int, str.rstrip(sys.stdin.readline()).split(' '))
    tx, ty = map(int, str.rstrip(sys.stdin.readline()).split(' '))

    queue = deque([(cy, cx)])
    visited = set()
    time = 0
    while queue :
        temp_queue = []
        while queue :
            y, x = queue.popleft()
            if y == ty and x == tx :
                queue, temp_queue = [], []
                answer_list.append(time)
                break
            if (y, x) in visited :
                continue
            visited.add((y, x))

            for dy, dx in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)] :
                if y+dy<0 or y+dy>=N or x+dx<0 or x+dx>N:
                    pass
                else :
                    temp_queue.append((y+dy, x+dx))
        if temp_queue :
            time += 1
            queue = deque(temp_queue)
            
for answer in answer_list:
    print(answer)