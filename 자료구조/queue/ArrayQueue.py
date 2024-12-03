import random

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


q = ArrayQueue(8)

q.display("초기상태 = ")
while not q.isFull():
    q.enqueue(random.randint(0,100))
q.display("포화상태 = ")

print("삭제순서 : ", end='')
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print()

