import sys

H, W = map(int, str.rstrip(sys.stdin.readline()).split(' '))
height_list = list(map(int, str.rstrip(sys.stdin.readline()).split(' ')))
arr = list(list(0 for _ in range(W)) for _ in range(H))
for index, height in enumerate(height_list):
    for h in range(H-height, H):
        arr[h][index] = 2

item_list = sorted(list(zip(height_list, list(index for index in range(W)))), key=lambda x : x[0])

for item in item_list:
    height, index = item
    if height == 0 : continue
    
    if list(filter(lambda x : x>=height, height_list[0:index])):
        for i in range(index-1, -1, -1):
            for h in range(H-height, H):
                if arr[h][i] != 2 :
                    arr[h][i] = 1
            if height_list[i] >= height : break
    
    if list(filter(lambda x : x>=height, height_list[index+1:W])):
        for i in range(index+1, W):
            for h in range(H-height, H):
                if arr[h][i] != 2 :
                    arr[h][i] = 1
            if height_list[i] >= height : break

rain = -sum(height_list)*2
for h in range(H):
    rain += sum(arr[h])
print(rain)