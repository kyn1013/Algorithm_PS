import collections

class Deq:

    def __init__(self):
        self.deque = collections.deque()

    def push_front(self, value):
        self.deque.appendleft(value)

    def push_back(self, value):
        self.deque.append(value)

    def pop_front(self):
        if len(self.deque) == 0:
            return -1

        return self.deque.popleft()

    def pop_back(self):
        if len(self.deque) == 0:
            return -1

        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def empty(self):
        if len(self.deque) == 0:
            return 1
        else:
            return 0

    def front(self):
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[0]

    def back(self):
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[-1]

deque = Deq()
n = int(input())
q = []
for _ in range(n):
    q.append(input().split())

for i in q:
    if i[0] == "pop_front":
        print(deque.pop_front())
    if i[0] == "pop_back":
        print(deque.pop_back())
    if i[0] == "size":
        print(deque.size())
    if i[0] == "empty":
        print(deque.empty())
    if i[0] == "front":
        print(deque.front())
    if i[0] == "back":
        print(deque.back())
    if i[0] == "push_front":
        deque.push_front(int(i[1]))
    if i[0] == "push_back":
        deque.push_back(int(i[1]))
