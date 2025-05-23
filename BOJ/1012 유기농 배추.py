from collections import deque
t = int(input())
ans = []
for i in range(t):
    m, n, c = map(int, input().split()) # 배추밭 가로길이, 세로길이, 배추가 심어져 있는 개수

    # 배추밭 세팅
    graph = []
    for _ in range(n):
        row = [0] * m
        graph.append(row)

    for _ in range(c):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 상하좌우 세팅
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(y, x):
        queue = deque()
        queue.append((y, x))
        graph[y][x] = 0

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if graph[ny][nx] == 0:
                    continue

                if graph[ny][nx] == 1:
                    queue.append((ny, nx))
                    graph[ny][nx] = 0



    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                count = count + 1
                BFS(y, x)

    ans.append(count)

for i in ans:
    print(i)
