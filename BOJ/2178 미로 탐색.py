from collections import deque

n, m = map(int, input().split()) # N × M 크기의 배열로 표현되는 미로, N개의 줄에 M개의 정수로 미로가 주어짐
maze = []

# 2차원 배열 만들기
for _ in range(n):
    row = input()
    row_list = list(row) # ['1', '0', '1', '0' ...]
    int_list = list(map(int, row_list)) # [1, 0, 1, 0 ...]
    maze.append(int_list)

# 상하좌우 방향
# x축과 y축을 움직이는 조합 : 왼쪽으로 움직이는 경우, 오른쪽으로 움직이는 경우, 아래로 가는 경우, 위로 가는 경우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 시작 좌표에서부터 상, 하, 좌, 우로 움직이는 경우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 skip
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 이동할 수 없는 칸이면 skip
            if maze[nx][ny] == 0:
                continue
            # 처음 방문하는 길이면 현재까지의 거리 + 1
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]

print(BFS(0, 0))




