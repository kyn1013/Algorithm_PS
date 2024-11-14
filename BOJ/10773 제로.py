count = int(input())
stack = []
ans = 0

for i in range(0, count):
    num = input()
    if int(num) == 0:
        stack.pop()
    else:
        stack.append(int(num))

for i in stack:
    ans += i

print(ans)
