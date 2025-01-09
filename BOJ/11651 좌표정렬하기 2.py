n = int(input())
arrays = []

for _ in range(n):
    x, y = map(int, input().split())
    arrays.append((x, y))

arrays.sort(key=lambda p: (p[1], p[0]))

for x, y in arrays:
    print(x, y)
