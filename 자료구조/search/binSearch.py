class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value #데이터 부분
        self.left = None
        self.right = None

def search_bst(n, key): #n==root
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def insert_bst(root, node):
    if root == None: #공백 노드에 도달하면 이 위치에 삽입
        return node
    if node.key == root.key: #동일한 키는 허용하지 않음
        return root

    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)

    return root

def delete_bst(root, key):
    if root == None:
        return root

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    #key와 root key와 같다면 root삭제
    else:

        #1. 단말 노드 또는 오른쪽 자식만 있는 경우
        if root.left == None:
            return root.right

        #2. 왼쪽 자식만 있는 경우
        elif root.right == None:
            return root.left

        #3. 두 자식이 모두 있는 경우
        succ = root.right
        while succ.left != None: #후계자 찾기
            succ = succ.left

        root.key = succ.key #후계자 값 복사
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key) #후계자 삭제

    return root
