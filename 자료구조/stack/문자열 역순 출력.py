class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self): return self.top == -1
    def isFull(self): return self.top == self.capacity -1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top +1]
        else:
            pass

    def peek(self):
        if not self.isFull():
            return self.array[self.top]
        else:
            pass

    def size(self): return self.top+1

s = ArrayStack(100)
msg = input("문자열 입력 :")
for c in msg:
    s.push(c)

print("문자열 출력: ", end = '')
while not s.isEmpty():
    print(s.pop(), end='')

print()


