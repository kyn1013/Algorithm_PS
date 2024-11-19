class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    def append(self, node): #self 다음에 node를 넣는 연산
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        next = self.link #현재 노드(self)의 다음 노드
        if next is not None:
            self.link = next.link
        return next


class LinkedList:
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
        node = Node(e, None)
        before = self.getNode(pos - 1)
        if before == None :
            node.link = self.head
            self.head = node
        else : before.append(node)

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else: return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count

    def display(self, msg='LinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            ptr = ptr.link
        print('None')

