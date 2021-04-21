
def cal(cur_coord):
    global M, min_k, max_k, max_hc
    y, x = cur_coord

    for k in range(min_k, max_k+1):
        profit = 0
        hc = 0
        for h_coord in house_coord :
            hy, hx = h_coord
            d = abs(y - hy) + abs(x - hx)
            if d < k :
                profit += M
                hc += 1
        profit = profit - (k*k + (k-1)*(k-1))
        if profit >=0 :
            max_hc = max(max_hc, hc)

if __name__ == '__main__':
    T = int(input().rstrip())
    for test_case in range(1, T+1):
        N, M = map(int, input().rstrip().split(' '))
        cost = M
        house_coord = []

        for y in range(N):
            temp_list = list(map(int, input().rstrip().split(' ')))
            for x in range(len(temp_list)):
                if temp_list[x] == 1 :
                    house_coord.append((y, x))
        max_hc = 0

        min_k = 1
        max_k = 2*N -2


        for y in range(N):
            for x in range(N):
                cal((y, x))

        print("#{} {}".format(test_case, max_hc))