import sys
import math


N, M = map(int, str.strip(sys.stdin.readline()).split(' '))

arr, pair = [], []
for _ in range(N):
    arr.append(int(str.strip(sys.stdin.readline())))

for _ in range(M):
    pair.append(list(map(int, str.strip(sys.stdin.readline()).split(' '))))

tree = list(sys.maxsize for _ in range(int(math.pow(2, math.ceil(math.log2(N))+1))))

def init_tree(start, end, arr, tree, index):
    if start == end :
        tree[index] = arr[start]
        return tree[index]
    else :
        tree[index] = min(init_tree(start, (start+end)//2, arr, tree, index*2), init_tree((start+end)//2+1, end, arr, tree, index*2+1))
        return tree[index]
def search(start, end, left, right, index, tree):
    if right < start or end < left : return sys.maxsize
    if left <= start and end <= right :
        return tree[index]
    return min(search(start, (start+end)//2, left, right, index*2, tree), search((start+end)//2+1, end, left, right, index*2+1, tree))
init_tree(0, N-1, arr, tree, 1)
for m in range(M):
    a, b = pair[m]
    print(search(1, N, a, b, 1, tree))

