import collections

class Queue:

    def __init__(self):
        self.queue = collections.deque()
        self.queueSize = 0

    def push(self, a):
        self.queue.appendleft(a)
        self.queueSize += 1

    def pop(self):
        if(self.queueSize > 0):
            print(self.queue.pop())
            self.queueSize -= 1
        else:
            print(-1)

    def size(self):
        print(self.queueSize)

    def empty(self):
        if self.queueSize == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if (self.queueSize > 0):
            print(self.queue[-1])
        else:
            print(-1)

    def back(self):
        if (self.queueSize > 0):
            print(self.queue[0])
        else:
            print(-1)

q = Queue()
n = int(input())
value = []
for i in range(n):
    value.append(input())

for i in value:
    if i == "front":
        q.front()
    elif i == "pop":
        q.pop()
    elif i == "size":
        q.size()
    elif i == "empty":
        q.empty()
    elif i == "back":
        q.back()
    else:
        k = i.split()
        num = k[1]
        q.push(num)
