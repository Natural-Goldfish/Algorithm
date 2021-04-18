from itertools import combinations
import sys

def cal_distance(coord_houses, coord_chickens):
    chicken_distance = 0
    for coord_house in coord_houses:
        my_chicken_distnance = sys.maxsize
        for coord_chicken in coord_chickens:
            y_h, x_h = coord_house
            y_c, x_c = coord_chicken
            d = abs(y_h - y_c) + abs(x_h - x_c)
            my_chicken_distnance = min(d, my_chicken_distnance)
        chicken_distance += my_chicken_distnance
    return chicken_distance

    
if __name__ == "__main__":
    H, M = map(int, sys.stdin.readline().rstrip().split(' '))
    arr = []
    coord_houses = []
    coord_chickens= []
    for y in range(H):
        temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        for x in range(len(temp)):
            if temp[x] == 1 :
                coord_houses.append((y, x))
            elif temp[x] == 2 :
                coord_chickens.append((y, x))
        arr.append(temp)
    possible_cases = combinations(coord_chickens, r=M)

    min_chicken_distance_city = sys.maxsize
    for chicken_coords in possible_cases:
        chicken_distance_city = cal_distance(coord_houses, chicken_coords)
        min_chicken_distance_city = min(chicken_distance_city, min_chicken_distance_city)
    print(min_chicken_distance_city)
    