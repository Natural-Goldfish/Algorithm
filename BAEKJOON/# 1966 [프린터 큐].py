import sys, heapq
from collections import deque

TEST_CASE = int(str.rstrip(sys.stdin.readline()))

for test_case in range(1, TEST_CASE+1):
    N, M = map(int, str.rstrip(sys.stdin.readline()).split(' '))
    arr = list(map(int, str.rstrip(sys.stdin.readline()).split(' ')))
    
    heap = list(map(lambda x : -x, arr))
    heapq.heapify(heap)

    arr = deque(list(zip(arr, list(index for index in range(len(arr))))))
    priority = -heapq.heappop(heap)
    index = 0
    while True :
        item = arr.popleft()
        
        if item[0] == priority :
            if item[1] == M :
                index += 1
                print(index)
                break
            else :
                priority = -heapq.heappop(heap)
                index += 1
        else :
            arr.append(item)
        