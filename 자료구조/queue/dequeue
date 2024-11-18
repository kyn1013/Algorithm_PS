class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass

    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self, msg):
        print(msg, end='[')
        for i in range(self.front + 1, (self.front + 1) + self.size()):
            print(self.array[i % self.capacity], end=' ')
        print(']')

class CircularDequeue(ArrayQueue):

    def __inti__(self, capacity = 10):
        super().__init__(capacity)

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass

    def addRear(self, item): self.enqueue(item)

    def deleteFront(self): return self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item

    def getFront(self): return self.peek()

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            pass

dq = CircularDequeue()

for i in range(8):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9,13): dq.addFront(i)
dq.display("전단에 9 ~ 13 삽입")
