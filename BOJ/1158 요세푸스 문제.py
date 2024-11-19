msg = input()
msgList = msg.split()
capacity = int(msgList[0])
start = int(msgList[1])
queue = []
ans = []
idx = 0

for i in range(1, capacity+1):
    queue.append(i)

idx = start - 1
ans.append(queue.pop(idx))
while len(queue) > 1:
    length = len(queue)
    ans.append(queue.pop((idx + start-1) % length))
    idx = (idx + start-1) % length

if len(queue) == 1:
    ans.append(queue.pop())
print('<', end='')
for i in ans:
    if i == ans[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print('>', end='')
