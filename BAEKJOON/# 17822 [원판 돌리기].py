import sys, copy
from collections import deque

class Circle():
    def __init__(self, number_list):
        self._number_list = deque(number_list)

    @property
    def number_list(self):
        return self._number_list

    @number_list.setter
    def number_list(self, new_list):
        self._number_list = new_list

    def rotate(self, direction, num):
        if direction == 0:
            for _ in range(num):
                self._number_list.appendleft(self._number_list.pop())
        else :
            for _ in range(num):
                self._number_list.append(self._number_list.popleft())

N, M, T = map(int, str.strip(sys.stdin.readline()).split(' '))
circle_list = [None]

for n in range(N):
    circle_list.append(Circle(list(map(int, str.strip(sys.stdin.readline()).split(' ')))))

for t in range(T):
    x, d, k = map(int, str.strip(sys.stdin.readline()).split(' '))
    if x == 1 :
        circle_list[x].rotate(d, k)
    else :
        for index in range(x, len(circle_list), x):
            circle_list[index].rotate(d, k)
    
    arr = list(circle_object.number_list for circle_object in circle_list[1:])
    new_arr = list(list() for _ in range(N))
    change_outer = True
    for n in range(N):
        cur_list, new_list = arr[n], copy.deepcopy(list(arr[n]))
        change = False

        for m in range(M):
            if m+1 == M and M != 1:
                if cur_list[-1] == cur_list[0] and cur_list[0] != 0:
                    new_list[0], new_list[-1] = 0, 0
                    change = True
            else :
                if cur_list[m] == cur_list[m+1] and cur_list[m] != 0:
                    new_list[m], new_list[m+1] = 0, 0
                    change = True

        before_list = arr[n-1] if n-1 >= 0 else []
        next_list = arr[n+1] if n+1 < N else []

        if next_list != []:    
            for m in range(M):
                if cur_list[m] == next_list[m] and cur_list[m] !=0 :
                    new_list[m] = 0
                    change = True            
        if before_list != [] :
            for m in range(M):
                if cur_list[m] == before_list[m] and cur_list[m] !=0 :
                    new_list[m] = 0
                    change = True            
        if change :
            new_arr[n] = new_list
            change_outer = False
    
    if change_outer :
        summary, numbers = 0, 0
        for circle_object in circle_list[1:] :
            temp = list(filter(lambda x : x !=0, circle_object.number_list))
            numbers += len(temp)
            summary += sum(temp)
        
        if numbers == 0 : continue
        avg = summary/numbers

        for circle_object in circle_list[1:] :
            target_list = circle_object.number_list
            for index in range(len(target_list)):
                if target_list[index] != 0 and target_list[index] < avg :
                    target_list[index] += 1
                elif target_list[index] != 0 and target_list[index] > avg:
                    target_list[index] -= 1
    else :
        for index, circle_object in enumerate(circle_list[1:]) :
            if new_arr[index] :
                circle_object.number_list = deque(new_arr[index])

print(sum(sum(circle_object.number_list) for circle_object in circle_list[1:]))
    