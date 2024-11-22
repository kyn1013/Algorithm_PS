class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

    def isLeft(self):
        return self.left is None and self.right is None

def preorder(root): #전위순회 -> 루 왼 오
    if root is not None:
        print(root.data, end='')
        preorder(root.left)
        preorder(root.right)

def inorder(root): #중위순회 -> 왼 루 오
    if root is not None:
        inorder(root.left)
        print(root.data, end='')
        inorder(root.right)

def postorder(root): #후위순회 -> 왼 오 루
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='')

def Build_Tree():
    count = int(input())
    node = {} #노드를 저장할 딕셔너리

    for _ in range(count):
        parent, left, right = input().split()

        if parent not in node:
            node[parent] = BTNode(parent)

        if left != '.':
            if left not in node:
                node[left] = BTNode(left)
            node[parent].left = node[left]

        if right != '.':
            if right not in node:
                node[right] = BTNode(right)
            node[parent].right = node[right]

    return node['A']

tree = Build_Tree()
preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
