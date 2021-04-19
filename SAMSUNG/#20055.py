import sys
from collections import deque

global info_dict, K

info_dict = {

}
def robot_move(belt1):
    global info_dict, K
    for x in range(len(belt1)-1, -1, -1):
        belt_number = belt1[x]
        if x == len(belt1)-1 and info_dict[belt_number][1] :
            info_dict[belt_number][1] = False
            continue
    
        if info_dict[belt_number][1] and not info_dict[belt1[x+1]][1] and info_dict[belt1[x+1]][0] >= 1:
            info_dict[belt_number][1] = False
            info_dict[belt1[x+1]][1] = True
            info_dict[belt1[x+1]][0] -= 1

            if info_dict[belt1[x+1]][0] == 0 :
                K -= 1
        
def belt_rotate(belt1, belt2):
    global info_dict
    if info_dict[belt1[-1]][1] :
        info_dict[belt1[-1]][1] = False

    first, last = belt2.popleft(), belt1.pop()
    belt2.append(last)
    return [first] + belt1

def robot_to_belt(belt1):
    global info_dict, K
    if not info_dict[belt1[0]][1] and info_dict[belt1[0]][0] >= 1:
        info_dict[belt1[0]][1] = True
        info_dict[belt1[0]][0] -= 1
        if info_dict[belt1[0]][0] == 0 :
            K -= 1

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split(' '))
    temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    belt1 = []
    for index in range(len(temp)//2):
        info_dict[index] = [temp[index], False]
        belt1.append(index)

    belt2 = deque([])
    for index in range(len(temp)-1, len(temp)//2 -1, -1):
        info_dict[index] = [temp[index], False]
        belt2.append(index)
    step = 0

    while K > 0 :
        belt1= belt_rotate(belt1, belt2)
        robot_move(belt1)
        robot_to_belt(belt1)
        step += 1
    print(step)