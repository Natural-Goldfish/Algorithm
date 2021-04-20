from itertools import product

# user 2명, 같은 좌표 있는것 가능, 지도 밖으로 나가는 경우 X
# BC에 들어오면 배터리 충전 가능
# 두 명이 동시에 접속 시, 배터리 균등하게 분배
# BC 여러개에 걸쳐 있으면 가장 좋은걸 택해야 함
# 초기 위치부터 충전 가능
global arr, bc_info, H, W, a_coord, a_charge, b_coord, b_charge

def makeArr():
    global arr, bc_info, H, W
    # BC 기반으로하여 Arr 재생성
    # BC1 = (by, bx, C, P), (y, x)에서 BC1 사용 가능 여부 "|y-by| + |x-bx| <= C"
    for y in range(H):
        for x in range(W):
            for bc_id, value_list in bc_info.items():
                by, bx, c, _ = value_list
                if abs(by-y) + abs(bx-x) <= c :
                    arr[y][x].append(bc_id)
     
    

def move(direction_a, direction_b):
    # 0 = 이동 x
    # 1 : UP
    # 2 : RIGHT
    # 3 : DOWN
    # 4 : Left
    direction = {
        0 : (0, 0),
        1 : (-1, 0),
        2 : (0, 1),
        3 : (1, 0),
        4 : (0, -1)
    }
    a_coord[0], a_coord[1] = a_coord[0] + direction[direction_a][0], a_coord[1] + direction[direction_a][1]
    b_coord[0], b_coord[1] = b_coord[0] + direction[direction_b][0], b_coord[1] + direction[direction_b][1]
    
def charge():
    global a_coord, a_charge, b_coord, b_charge, arr

    ay, ax = a_coord
    by, bx = b_coord
    bc_id_list_a = arr[ay][ax]
    bc_id_list_b = arr[by][bx]

    if bc_id_list_a and bc_id_list_b :    # 둘 다 충전 가능한 경우
        possible_cases = list(product(*[bc_id_list_a, bc_id_list_b]))
        max_p = (0, 0, 0)   # sum, a, b
        for ids in possible_cases :
            bc_id_a, bc_id_b = ids
            cur_p = (0, 0, 0)
            if bc_id_a == bc_id_b :
                sum_p = (bc_info[bc_id_a][3])//2
                cur_p = (sum_p, sum_p, sum_p)
            else :
                cur_p_a, cur_p_b = bc_info[bc_id_a][3], bc_info[bc_id_b][3]
                sum_p = cur_p_a + cur_p_b
                cur_p = (sum_p, cur_p_a, cur_p_b)
            if max(cur_p[0], max_p[0]) == cur_p[0] :
                max_p = cur_p
        a_charge += max_p[1]
        b_charge += max_p[2]

    elif bc_id_list_a and not bc_id_list_b:
        max_p = 0
        for bc_id in bc_id_list_a :
            max_p = max(max_p, bc_info[bc_id][3])
        a_charge += max_p

    elif not bc_id_list_a and bc_id_list_b:
        max_p = 0
        for bc_id in bc_id_list_b :
            max_p = max(max_p, bc_info[bc_id][3])
        b_charge += max_p

if __name__ == "__main__":
    T = int(input().rstrip())
    H, W = 10, 10
    for test_case in range(1, T+1):
        _, A = map(int, input().rstrip().split(' '))
        
        a_move, a_coord, a_charge = list(map(int, input().rstrip().split(' '))), [0, 0], 0
        b_move, b_coord, b_charge = list(map(int, input().rstrip().split(' '))), [9 ,9], 0

        bc_info = {}
        bc_id = 0
        for i in range(A):
            x, y, c, p = map(int, input().rstrip().split(' '))
            bc_info[bc_id] = [y-1, x-1, c, p]
            bc_id += 1

        arr = [[ [] for _ in range(W)] for _ in range(H)]
        makeArr()

        charge()
        for index in range(len(a_move)):
            a_direction, b_direction = a_move[index], b_move[index]
            move(a_direction, b_direction)
            charge()

        
        print("#{} {}".format(test_case, a_charge + b_charge))