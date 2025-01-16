import collections

n_count = int(input())
ans = []

for _ in range(n_count):
    deque = collections.deque()
    seq = collections.deque()

    n, m = map(int, input().split())

    numbers = map(int, input().split())
    index = 0
    for i in numbers:
        deque.append(i)
        seq.append(index)
        index += 1

    count = 0
    max_value = max(deque)

    while m in seq:
        if deque[0] != max_value:
            deque.rotate(-1)
            seq.rotate(-1)
        else:
            deque.popleft()
            seq.popleft()
            count += 1
            if len(deque):
                max_value = max(deque)

    ans.append(count)

for i in ans:
    print(i)
