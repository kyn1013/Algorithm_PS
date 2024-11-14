class Stack:

    def __init__(self):
        self.idx = -1
        self.stack = []

    def push(self, number):
        self.idx += 1
        self.stack.append(number)

    def pop(self):
        if (len(self.stack) == 0):
            return -1
        else:
            self.idx -= 1
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if(len(self.stack) == 0):
            return 1
        else:
            return 0

    def top(self):
        if(len(self.stack) == 0):
            return -1
        else:
            return self.stack[self.idx]

listStack = Stack()
ans = []
count = int(input())
for i in range(0, count):
    ans.append(input())

for i in ans:
    if i == "top":
        print(listStack.top())
    elif i == "pop":
        print(listStack.pop())
    elif i == "size":
        print(listStack.size())
    elif i == "empty":
        print(listStack.empty())
    else:
        push = i.split()
        num = int(push[1])
        listStack.push(num)
