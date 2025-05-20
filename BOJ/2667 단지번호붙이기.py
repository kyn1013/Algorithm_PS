from collections import deque
n = int(input()) # n * n 형태의 지도의 크기

# 지도 세팅
maze = []
for _ in range(n):
    row = input()
    char_row = list(row)
    int_row = list(map(int, char_row))
    maze.append(int_row)

# 상하좌우 좌표 세팅
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    maze[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위가 안되면 skip
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue

            # 0 이라면 skip
            if maze[nx][ny] == 0:
                continue

            # 탐색 할 수 있는 범위라면 count 증가
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = 0
                count = count + 1

    return count

aprt = []
ans = 0

# 지도 탐색 시작
for i in range(n):
    for j in range(n):
        if maze[i][j] == 1:
            aprt.append(BFS(i, j))
            ans = ans + 1

aprt.sort()
print(ans)
for i in aprt:
    print(i)
