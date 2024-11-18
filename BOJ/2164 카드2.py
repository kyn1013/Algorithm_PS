import queue
import collections

card = int(input())

qu = collections.deque()
for i in range(1, card+1):
    qu.append(i)

idx = 1
while 1:
    if len(qu) == 1:
        break
    if idx % 2 != 0:
        qu.popleft()
        idx += 1
    else:
        item = qu.popleft()
        qu.append(item)
        idx += 1

print(qu.popleft())
