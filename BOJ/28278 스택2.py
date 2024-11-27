import sys
input = sys.stdin.read  # 빠른 입력 사용
data = input().splitlines()  # 모든 입력을 한 번에 가져옴

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        return self.stack.pop() if self.stack else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        return self.stack[-1] if self.stack else -1

listStack = Stack()
ans = []

# 첫 줄: 명령 개수
count = int(data[0])

# 나머지 명령 처리
for i in range(1, count + 1):
    command = data[i]
    if command == "5":
        ans.append(listStack.top())
    elif command == "2":
        ans.append(listStack.pop())
    elif command == "3":
        ans.append(listStack.size())
    elif command == "4":
        ans.append(listStack.empty())
    else:  # "1 X" 형태
        _, num = command.split()
        listStack.push(int(num))


sys.stdout.write("\n".join(map(str, ans)) + "\n")
