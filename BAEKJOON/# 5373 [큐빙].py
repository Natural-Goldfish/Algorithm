import sys, copy

class Cube():
    def __init__(self):
        self.U = list(list('w' for _ in range(3)) for _ in range(3)) # 윗 면
        self.D = list(list('y' for _ in range(3)) for _ in range(3)) # 아랫 면
        self.F = list(list('r' for _ in range(3)) for _ in range(3)) # 앞 면
        self.B = list(list('o' for _ in range(3)) for _ in range(3)) # 뒷 면
        self.L = list(list('g' for _ in range(3)) for _ in range(3)) # 왼쪽 면
        self.R = list(list('b' for _ in range(3)) for _ in range(3)) # 오른쪽 면

    def rotate(self, side, direction):
        if side == 'U' :
            if direction == '+':
                for index in range(3):
                    self.F[0][index], self.R[0][index], self.B[0][index], self.L[0][index] =\
                        self.R[0][index], self.B[0][index], self.L[0][index], self.F[0][index]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.U[y][x], self.U[2-x][y], self.U[2-y][2-x], self.U[x][2-y] =\
                            self.U[2-x][y], self.U[2-y][2-x], self.U[x][2-y], self.U[y][x]
            elif direction == '-' :
                for index in range(3):
                    self.F[0][index], self.R[0][index], self.B[0][index], self.L[0][index] =\
                        self.L[0][index], self.F[0][index], self.R[0][index], self.B[0][index],  
                for y in range(2):
                    for x in range(y, 2-y):
                        self.U[y][x], self.U[x][2-y], self.U[2-y][2-x], self.U[2-x][y] =\
                            self.U[x][2-y], self.U[2-y][2-x], self.U[2-x][y], self.U[y][x]                             
        elif side == 'F' :
            if direction == '+':
                for index in range(3):
                    self.U[-1][2-index], self.R[2-index][0], self.D[0][index], self.L[index][-1] =\
                        self.L[index][-1], self.U[-1][2-index], self.R[2-index][0], self.D[0][index]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.F[y][x], self.F[2-x][y], self.F[2-y][2-x], self.F[x][2-y] =\
                            self.F[2-x][y], self.F[2-y][2-x], self.F[x][2-y], self.F[y][x]
            elif direction == '-' :
                for index in range(3):
                    self.U[-1][2-index], self.R[2-index][0], self.D[0][index], self.L[index][-1] =\
                        self.R[2-index][0], self.D[0][index], self.L[index][-1], self.U[-1][2-index] 
                for y in range(2):
                    for x in range(y, 2-y):
                        self.F[y][x], self.F[x][2-y], self.F[2-y][2-x], self.F[2-x][y] =\
                            self.F[x][2-y], self.F[2-y][2-x], self.F[2-x][y], self.F[y][x]                             
        elif side == 'L':
            if direction == '+':
                for index in range(3):
                    self.U[2-index][0], self.F[2-index][0], self.D[2-index][0], self.B[index][-1] =\
                        self.B[index][-1], self.U[2-index][0], self.F[2-index][0], self.D[2-index][0]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.L[y][x], self.L[2-x][y], self.L[2-y][2-x], self.L[x][2-y] =\
                            self.L[2-x][y], self.L[2-y][2-x], self.L[x][2-y], self.L[y][x]
            elif direction == '-' :
                for index in range(3):
                    self.U[2-index][0], self.F[2-index][0], self.D[2-index][0], self.B[index][-1] =\
                        self.F[2-index][0], self.D[2-index][0], self.B[index][-1], self.U[2-index][0],  
                for y in range(2):
                    for x in range(y, 2-y):
                        self.L[y][x], self.L[x][2-y], self.L[2-y][2-x], self.L[2-x][y] =\
                            self.L[x][2-y], self.L[2-y][2-x], self.L[2-x][y], self.L[y][x]                              
        elif side == 'R':
            if direction == '+':
                for index in range(3):
                    self.U[index][-1], self.F[index][-1], self.D[index][-1], self.B[2-index][0] =\
                        self.F[index][-1], self.D[index][-1], self.B[2-index][0], self.U[index][-1]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.R[y][x], self.R[2-x][y], self.R[2-y][2-x], self.R[x][2-y] =\
                            self.R[2-x][y], self.R[2-y][2-x], self.R[x][2-y], self.R[y][x]
            elif direction == '-' :
                for index in range(3):
                    self.U[index][-1], self.B[2-index][0], self.D[index][-1], self.F[index][-1],  =\
                        self.B[2-index][0], self.D[index][-1], self.F[index][-1], self.U[index][-1]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.R[y][x], self.R[x][2-y], self.R[2-y][2-x], self.R[2-x][y] =\
                            self.R[x][2-y], self.R[2-y][2-x], self.R[2-x][y], self.R[y][x]                                                  
        elif side == 'B':
            if direction == '+':
                for index in range(3):
                    self.U[0][index], self.R[index][-1], self.D[-1][2-index], self.L[2-index][0] =\
                        self.R[index][-1], self.D[-1][2-index], self.L[2-index][0], self.U[0][index]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.B[y][x], self.B[2-x][y], self.B[2-y][2-x], self.B[x][2-y] =\
                            self.B[2-x][y], self.B[2-y][2-x], self.B[x][2-y], self.B[y][x]
            elif direction == '-' :
                for index in range(3):
                    self.U[0][index], self.R[index][-1], self.D[-1][2-index], self.L[2-index][0] =\
                        self.L[2-index][0], self.U[0][index], self.R[index][-1], self.D[-1][2-index]
                for y in range(2):
                    for x in range(y, 2-y):
                        self.B[y][x], self.B[x][2-y], self.B[2-y][2-x], self.B[2-x][y] =\
                            self.B[x][2-y], self.B[2-y][2-x], self.B[2-x][y], self.B[y][x]       
        elif side == 'D':
            if direction == '+':
                for index in range(3):
                    self.F[-1][index], self.R[-1][index], self.B[-1][index], self.L[-1][index] =\
                        self.L[-1][index], self.F[-1][index], self.R[-1][index], self.B[-1][index]            
                for y in range(2):
                    for x in range(y, 2-y):
                        self.D[y][x], self.D[2-x][y], self.D[2-y][2-x], self.D[x][2-y] =\
                            self.D[2-x][y], self.D[2-y][2-x], self.D[x][2-y], self.D[y][x]
            elif direction == '-' :
                for index in range(3):
                    self.F[-1][index], self.R[-1][index], self.B[-1][index], self.L[-1][index] =\
                        self.R[-1][index], self.B[-1][index], self.L[-1][index], self.F[-1][index],  
                for y in range(2):
                    for x in range(y, 2-y):
                        self.D[y][x], self.D[x][2-y], self.D[2-y][2-x], self.D[2-x][y] =\
                            self.D[x][2-y], self.D[2-y][2-x], self.D[2-x][y], self.D[y][x]

''' rotation check
temp_list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for temp in temp_list:
    print(temp)
for y in range(2):
    for x in range(y, 2-y):
        temp_list[y][x], temp_list[x][2-y], temp_list[2-y][2-x], temp_list[2-x][y] =\
            temp_list[x][2-y], temp_list[2-y][2-x], temp_list[2-x][y], temp_list[y][x]
for temp in temp_list:
    print(temp)
for y in range(2):
    for x in range(y, 2-y):
        temp_list[y][x], temp_list[2-x][y], temp_list[2-y][2-x], temp_list[x][2-y] =\
            temp_list[2-x][y], temp_list[2-y][2-x], temp_list[x][2-y], temp_list[y][x]    
for temp in temp_list:
    print(temp)
'''
TEST_CASE = int(str.strip(sys.stdin.readline()))
answer_list = []
for test_case in range(1, TEST_CASE+1):
    n = int(str.strip(sys.stdin.readline()))
    order_list = str.strip(sys.stdin.readline()).split(' ')
    cube = Cube()
    for order in order_list:
        cube.rotate(order[0], order[1])
    
    answer_list += list(''.join(temp) for temp in cube.U)

for answer in answer_list:
    print(answer)

