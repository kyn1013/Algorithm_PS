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

def checkBrackets(str):
    stack = ArrayStack(100)
    for ch in str:
        if ch in ('(','{','['):
            stack.push(ch)
        elif ch in (')','}',']'):
            if stack.isEmpty():
                return False #오른쪽 괄호가 먼저 나온 경우
            else :
                left = stack.pop()
                if(left == "(" and ch != ")" ) or (left == "{" and ch != "}") or (left == "[" and ch != "]") :
                    return False #괄호 쌍이 맞지 않는 경우

    return stack.isEmpty() #괄호가 남아았다면 괄호 쌍의 수가 다른 것

print(checkBrackets("{(a+b)+(c+d)}"))

