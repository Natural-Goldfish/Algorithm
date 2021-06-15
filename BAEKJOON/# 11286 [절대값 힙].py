import sys, heapq

N = int(str.rstrip(sys.stdin.readline(), ''))
heap, answer = [], []
for _ in range(N):
    number = int(str.rstrip(sys.stdin.readline(), ''))
    if number == 0 :
        if heap :
            abs_number, true_number = heapq.heappop(heap)
            answer.append(true_number)
        else :
            answer.append(0)
    else :
        heapq.heappush(heap, (abs(number), number))
for number in answer :
    print(number)