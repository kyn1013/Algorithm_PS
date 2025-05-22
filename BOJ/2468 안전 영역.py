from collections import deque
n = int(input()) # n * n 지도

# 지도 세팅
graph = []

for _ in range(n):
    row = input()
    row_list = list(map(int, row.split()))
    graph.append(row_list)

# 상하좌우 세팅
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, g):
    queue = deque()
    queue.append((x, y))
    g[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if g[nx][ny] == 0:
                continue
            if g[nx][ny] != 0:
                queue.append((nx, ny))
                g[nx][ny] = 0

# 0부터 100까지 높이로 물에 잠긴다고 가정했을 때 뮬애 안 잠기는 가장 큰 수가 정답 (아무 지역도 물에 안 잠기는 경우도 있으므로 0부터 시작해야 함)
ans = []
for i in range(0, 101):
    area = 0
    # 그래프 세팅
    g = [row[:] for row in graph]
    for x in range(n):
        for y in range(n):
            if g[x][y] <= i:
                g[x][y] = 0

    for x in range(n):
        for y in range(n):
            if g[x][y] != 0:
                area = area + 1
                BFS(x, y, g)

    ans.append(area)

print(max(ans))
