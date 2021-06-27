import sys
from collections import deque
N = int(str.rstrip(sys.stdin.readline()))
K = int(str.rstrip(sys.stdin.readline()))

arr = list(list(0 for _ in range(N)) for _ in range(N))
for _ in range(K):
    row, column = map(int, str.rstrip(sys.stdin.readline()).split(' '))
    arr[row-1][column-1] = 1

L = int(str.rstrip(sys.stdin.readline()))
move_list = list(tuple(str.rstrip(sys.stdin.readline()).split(' ')) for _ in range(L))
move_list.reverse()

class Snake():
    def __init__(self):
        self._direction = 'R'
        self.coord = deque([(0, 0)])
        self._cur_coord = self.coord[-1]
        self.flag = False

    @property
    def cur_coord(self):
        self._cur_coord = self.coord[-1]
        return self._cur_coord
    @cur_coord.setter
    def cur_coord(self, new_coord):
        self._cur_coord = new_coord

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if direction == 'D':
            if self.direction == 'R':
                self._direction = 'D'
            elif self.direction == 'L':
                self._direction = 'U'
            elif self.direction == 'D':
                self._direction = 'L'
            elif self.direction == 'U' :
                self._direction = 'R'
        else :
            if self.direction == 'R':
                self._direction = 'U'
            elif self.direction == 'L':
                self._direction = 'D'
            elif self.direction == 'D':
                self._direction = 'R'
            elif self.direction == 'U' :
                self._direction = 'L'

    def move(self, arr):
        # 머리 이동
        if self.direction == 'R' :
            dy, dx = 0, 1
        elif self.direction == 'L' :
            dy, dx = 0, -1
        elif self.direction == 'D' :
            dy, dx = 1, 0
        else :
            dy, dx = -1, 0
        y, x = self.coord[-1]
        head_coord = (y+dy, x+dx)
        self.coord.append(head_coord)

        # 벽 충돌 검사
        if head_coord[0]<0 or head_coord[0]>=len(arr) or head_coord[1]<0 or head_coord[1]>=len(arr):
            pass
        else :
            y, x = head_coord
            if arr[y][x] == 1 :
                arr[y][x] = 0
            else :
                self.flag = True

    def move2(self):
        if self.flag :
            self.coord.popleft()
            self.flag = False
time = 0
snake = Snake()
while True :
    snake.move(arr)

    time += 1

    y, x = snake.cur_coord
    if y<0 or y>=len(arr) or x<0 or x>=len(arr) or (y, x) in set(list(snake.coord)[:-1]):
        print(time)
        break

    snake.move2()

    if move_list :
        if int(move_list[-1][0]) == time :
            item = move_list.pop()
            snake.direction = item[1]