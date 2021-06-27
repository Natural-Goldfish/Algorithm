import sys
from collections import deque
sys.setrecursionlimit(10000)

class Node :
    def __init__(self, data):
        self._parent = None
        self._data = data
        self._children = []
    
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, node):
        self._parent = node
    
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def children(self):
        return self._children
    @children.setter
    def children(self, node_list):
        self._children = list(node_list)


def init_tree(node_dict, node_list):
    root = 1
    queue = deque(list(zip(node_dict[root], list(root for _ in range(len(node_dict[root]))))))
    visited = set()
    while queue :
        child_num, parent_num= queue.popleft()
        if child_num == parent_num : continue
        if (child_num, parent_num) in visited : continue
        node_list[child_num-1].parent = parent_num
        visited.add((child_num, parent_num))

        node_dict[child_num].remove(parent_num)
        queue += list(zip(node_dict[child_num], list(child_num for _ in range(len(node_dict[child_num])))))

N = int(str.rstrip(sys.stdin.readline()))
node_dict = {}
node_list = [Node(index+1) for index in range(N)]

for n in range(N-1):
    a, b = map(int, str.rstrip(sys.stdin.readline()).split(' '))
    if a in node_dict :
        node_dict[a].append(b)
    else :
        node_dict[a] = [b]
    
    if b in node_dict :
        node_dict[b].append(a)
    else :
        node_dict[b] = [a]

init_tree(node_dict, node_list)

for node in node_list[1:] :
    print(node.parent)