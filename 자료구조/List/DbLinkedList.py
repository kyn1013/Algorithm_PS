class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.next = next
        self.prev = prev

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def popNext(self): #self 다음 노드 삭제 연산
        node = self.next #삭제할 노드
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node


class DbLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0 : return None
        ptr = self.head # 시작위치 -> head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr # 최종 노드 반환

    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None: return None #해당 노드가 없는 경우
        else: return node.data #있는 경우 데이터 필드 반환

    def insert(self, pos, e):
        node = DNode(e, None)
        before = self.getNode(pos - 1)
        if before == None :
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else: before.append(node)

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else: return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count

    def display(self, msg='DbLinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next
        print('None')
