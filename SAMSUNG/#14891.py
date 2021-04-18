
from collections import deque

# 톱니바퀴 회전

# 양 옆에 회전 시켜야 하는지 여부 + 회전한 톱니바퀴는 제외
global N, RIGHT, LEFT, machine
N, RIGHT, LEFT = 4, 2, 6
machine = {
    0 : None,
    1 : None,
    2 : None,
    3 : None
}

def bfs(info, turned):
    global machine, RIGHT, LEFT
    queue = deque([info])
    while queue :
        machine_num, direction = queue.popleft()

        left, right = machine[machine_num][LEFT], machine[machine_num][RIGHT]
        rotate(machine_num, direction)
        turned[machine_num] = True

        left_machine_num, right_machine_num = machine_num-1, machine_num + 1

        # Left
        if left_machine_num < 0 : pass
        else :
            if not turned[left_machine_num] and machine[left_machine_num][RIGHT] != left :
                if direction == -1 : 
                    queue.append((left_machine_num, 1))
                else : 
                    queue.append((left_machine_num, -1))

        # Right
        if right_machine_num > 3 : pass
        else :
            if not turned[right_machine_num] and machine[right_machine_num][LEFT] != right :
                if direction == -1 : 
                    queue.append((right_machine_num, 1))
                else : 
                    queue.append((right_machine_num, -1))



def rotate(machine_num, rotate_dir):
    global machine
    if rotate_dir == 1:             # 시계방향
        temp = machine[machine_num].pop()
        machine[machine_num] = deque([temp]) + machine[machine_num]
    elif rotate_dir == -1 :         # 반시계
        temp = machine[machine_num].popleft()
        machine[machine_num].append(temp)

if  __name__ == "__main__":
    for n in range(N):
        machine[n] = deque([int(char) for char in input().rstrip()])
    num_case = int(input().rstrip())
    cases = []
    for i in range(num_case):
        machine_num, rotation_dir = map(int, input().rstrip().split(' '))
        cases.append((machine_num-1, rotation_dir))
    
    for case in cases:
        turned = [False for _ in range(N)]
        bfs(case, turned)
    
    point = 0
    for n in range(N):
        if machine[n][0] == 1 :
            point += 2**n
    print(point)