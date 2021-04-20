
from collections import deque
# clock-wise : 1
# counter clock-wise : -1
# N : 0
# S : 1
# clock-wise input
# max-magnetic-num : 4
# blade per magnetic : 8

global LEFT, RIGHT

LEFT = 6
RIGHT = 2

def work(info, visited):
    global LEFT, RIGHT, m_dict

    queue = deque([info])
    while queue :
        m_number, direction = queue.popleft()

        if visited[m_number-1] == True : continue
        visited[m_number-1] = True
        # LEFT
        l_number = m_number - 1
        if l_number < 1 : pass    
        else :
            if visited[l_number -1] == True : 
                pass
            else :
                if m_dict[l_number][RIGHT] != m_dict[m_number][LEFT]:
                    if direction == 1 :
                        queue.append((l_number, -1))
                    else :
                        queue.append((l_number, 1))
                    
        # RIGHT
        r_number = m_number + 1
        if r_number > 4 : pass
        else :
            if visited[r_number -1] == True : 
                pass
            else :
                if m_dict[r_number][LEFT] != m_dict[m_number][RIGHT] :
                    if direction == 1 :
                        queue.append((r_number, -1))
                    else :
                        queue.append((r_number, 1))
        rotate(m_number, direction)

def rotate(machine_num, direction):
    global m_dict
    if direction == 1 :
        temp_list = m_dict[machine_num]
        f = temp_list.pop()
        m_dict[machine_num] = deque([f]) + temp_list
    else :
        l = m_dict[machine_num].popleft()
        m_dict[machine_num].append(l)

if __name__ == "__main__":
    T = int(input().rstrip())
    for test_case in range(1, T+1):
        K = int(input().rstrip())

        m_dict = {}
        for i in range(4):
            m_dict[i+1] = deque(list(map(int, input().rstrip().split(' '))))

        rotation_case = []
        for num in range(K):
            rotation_case.append(list(map(int, input().rstrip().split(' '))))

        for item in rotation_case :
            machine_num, direction = item
            visited = [False for _ in range(4)]
            work((machine_num, direction), visited)
        
        point = 0
        for m_number, temp_list in m_dict.items():
            if temp_list[0] == 1 :
                point += 2**(m_number-1)
        print("#{} {}".format(test_case, point))

        