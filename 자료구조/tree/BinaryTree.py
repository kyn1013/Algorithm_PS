from 자료구조.queue.ArrayQueue import ArrayQueue

class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left #왼쪽 자식을 위한 링크
        self.right = right #오른쪽 자식을 위한 링크

def preorder(n): #전위순회
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n): #중위순회
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n): #후위순회
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


def levelorder(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f = BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A', b, c)

print('\n   In-Order : ', end=''); inorder(root)
print('\n  Pre-Order : ', end=''); preorder(root)
print('\n Post-Order : ', end=''); postorder(root)
print('\nLevel-Order : ', end=''); levelorder(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 트리의 높이 = %d" % calc_height(root))
