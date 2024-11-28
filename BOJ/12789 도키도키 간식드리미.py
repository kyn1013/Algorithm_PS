n = int(input())
num = list(map(int, input().split()))
stack = [0]*n
ans = "Nice"
k = 1
idx = 0
while k <= n:
    while stack[-1] != k and idx < n:
        stack.append(num[idx])
        idx += 1

    if len(stack) and stack[-1] == k:
        stack.pop()
        k += 1
    else:
        ans = "Sad"
        break

print(ans)
