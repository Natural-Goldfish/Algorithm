import sys
from collections import deque

prime_numbers_under100 = [number for number in range(1, 101)]
for number in [2, 3, 5, 7, 9]:
    prime_numbers_under100 = list(filter(lambda x : x%number != 0, prime_numbers_under100))
prime_numbers = [number for number in range(1000, 10000)]
for number in [2, 3, 5, 7, 9] + prime_numbers_under100[1:]:
    prime_numbers = list(filter(lambda x : x%number !=0, prime_numbers))

def bfs(src, dst, prime_numbers):
    queue = deque([src])
    visited = set([])
    count = 0
    while queue :
        temp_queue = []

        while queue :
            cur = queue.popleft()
            if cur == dst :
                return count
            visited.add(cur)

            for position in range(4):
                for number in range(10):
                    if position == 0 and number == 0: continue
                    if number == int(str(cur)[position]) : continue
                    possible_number = int(''.join(list(str(cur)[index] if (index != position) else str(number) for index in range(4))))

                    if possible_number in prime_numbers and possible_number not in visited :
                        temp_queue.append(possible_number)

        if temp_queue :

            queue = deque(list(set(temp_queue)))
            count += 1

    return 'Impossible'

answer_list = []
TEST_CASE = int(str.strip(sys.stdin.readline()))
for test_case in range(1, TEST_CASE+1):
    src, dst = str.strip(sys.stdin.readline()).split(' ')
    answer_list.append(bfs(int(src), int(dst), set(prime_numbers)))
for answer in answer_list :
    print(answer)


    
        