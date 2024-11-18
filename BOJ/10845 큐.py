class Queue:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front_idx = 0
        self.rear = 0
        self.array = [None]*capacity

    def empty(self):
        if self.front_idx == self.rear:
            return 1
        else:
            return 0

    def push(self, item):
        if not self.size() == self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            return -1

    def pop(self):
        if not self.empty():
            self.front_idx = (self.front_idx + 1) % self.capacity
            return self.array[self.front_idx]
        else:
            return -1

    def size(self):
        return (self.rear - self.front_idx + self.capacity) % self.capacity

    def front(self):
        if not self.empty():
            return self.array[(self.front_idx + 1) % self.capacity]
        else:
            return -1

    def back(self):
        if not self.empty():
            return self.array[self.rear]
        else:
            return -1


count = int(input())
inputList = []
arrQueue = Queue(count+1)

for i in range(count):
    inputList.append(input())

for i in inputList:
    if i == 'pop':
        print(arrQueue.pop())
    elif i == 'size':
        print(arrQueue.size())
    elif i == 'empty':
        if arrQueue.size() == 0:
            print(1)
        else:
            print(0)
    elif i == 'front':
        print(arrQueue.front())
    elif i == 'back':
        print(arrQueue.back())
    else:
        strList = i.split()
        arrQueue.push(int(strList[1]))
