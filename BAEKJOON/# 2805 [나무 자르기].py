import sys

N, M  = map(int, str.rstrip(sys.stdin.readline(), '').split(' '))
tree_list = list(map(int, str.rstrip(sys.stdin.readline(), '').split(' ')))
height_min, height_max = 0, 1000000000
last = False
while True :
    height = (height_min + height_max)//2
    if height_max - height_min == 1 :
        last = True
    if not last :
        gain = sum(tree_height - height if height < tree_height else 0 for tree_height in tree_list)
    if 0 <= gain < M :
        height_max = height
    elif M < gain :
        height_min = height
    else :
        print(height)
        break
    if last :
        gain_min = sum(tree_height - height_min if height_min < tree_height else 0 for tree_height in tree_list)
        gain_max = sum(tree_height - height_max if height_max < tree_height else 0 for tree_height in tree_list)
        if gain_max < M :
            print(height_min)
        else :
            print(height_max)
        break