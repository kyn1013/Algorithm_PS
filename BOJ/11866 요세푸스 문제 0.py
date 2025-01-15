import collections
n, k = map(int, input().split())

deque = collections.deque()
ans = []

for i in range(1, n+1):
    deque.append(i)

idx = 0
while 0 < len(deque):
    idx = (idx + 2) % len(deque)
    #rotate가 음수라면 앞쪽에 있는 요소가 해당 갯수만큼 뒤쪽으로 감
    deque.rotate(-(k-1))
    ans.append(deque.popleft())

print("<", end="")
for i in ans[:-1]:
    print(str(i)+", ", end="")
print(ans[-1], end="")
print(">", end="")
