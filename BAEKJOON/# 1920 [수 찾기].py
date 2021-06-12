import sys

class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree :
    def __init__(self, root):
        self.root = root
    
    def insert(self, node):
        cur_node = self.root
        while cur_node :
            if cur_node.data < node.data :
                if cur_node.right == None :
                    cur_node.right = node
                    break
                else :
                    cur_node = cur_node.right
            else :
                if cur_node.left == None :
                    cur_node.left = node
                    break
                else :
                    cur_node = cur_node.left
    def search(self, num):
        cur_node = self.root

        while cur_node :
            if cur_node.data < num :
                if cur_node.right :
                    cur_node = cur_node.right
                else :
                    return 0
            elif cur_node.data > num :
                if cur_node.left :
                    cur_node = cur_node.left
                else :
                    return 0
            else :
                return 1

N = int(str.rstrip(sys.stdin.readline()))
numbers = list(map(int, str.rstrip(sys.stdin.readline()).split(' ')))
bst = BinarySearchTree(Node(numbers[0]))
for num in numbers[1:]:
    bst.insert(Node(num))

N = int(str.rstrip(sys.stdin.readline()))
numbers = list(map(int, str.rstrip(sys.stdin.readline()).split(' ')))
for num in numbers :
    print(bst.search(num))