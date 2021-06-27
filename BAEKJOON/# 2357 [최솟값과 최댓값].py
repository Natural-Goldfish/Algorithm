import sys, math

class SegmentTree:
    def __init__(self, arr):
        self._MIN = -sys.maxsize
        self._MAX = sys.maxsize
        self.tree = [None for _ in range(int(math.pow(2, 1+math.ceil(math.log2(len(arr))))))]
        self.tree_init(1, len(arr), arr)

    def tree_init(self, start, end, arr, index=1):
        if start == end :
            self.tree[index] = (arr[start-1], arr[start-1])
        else :
            left_tree = self.tree_init(start, (start+end)//2, arr, index*2)
            right_tree = self.tree_init((start+end)//2 + 1, end, arr, index*2 + 1)
            min_value, max_value = min(left_tree[0], right_tree[0]),max(left_tree[1], right_tree[1])
            self.tree[index] = (min_value, max_value)
        return self.tree[index]

    def search(self, start, end, left, right, index=1):
        if end < left or right < start :
            return (self._MAX, self._MIN)
        if left <= start and end <= right :
            return self.tree[index]
        else :
            left_tree = self.search(start, (start+end)//2, left, right, index*2)
            right_tree = self.search((start+end)//2 + 1, end, left, right, index*2 + 1)
            return min(left_tree[0], right_tree[0]),max(left_tree[1], right_tree[1])
    
    def update(self, start, end, t_index, value, index=1):
        if t_index < start or end < t_index :
            return
        if start == end and start == t_index :
            self.tree[index] = (value, value)
            return self.tree[index]
        elif start <= t_index and t_index <= end :
            left_tree = self.update(start, (start+end)//2, t_index, value, index*2)
            right_tree = self.update((start+end)//2 + 1, end, t_index, value, index*2 + 1)
            self.tree[index] = min(left_tree[0], right_tree[0]),max(left_tree[1], right_tree[1])
            return self.tree[index]
    
N, M = map(int, str.rstrip(sys.stdin.readline()).split(' '))
numbers = [int(str.rstrip(sys.stdin.readline())) for _ in range(N)]
range_list = [map(int, str.rstrip(sys.stdin.readline()).split(' ')) for _ in range(M)]
st = SegmentTree(numbers)
for ab in range_list:
    a, b = ab
    min_value, max_value = st.search(1, N, a, b)
    print(min_value, max_value)
