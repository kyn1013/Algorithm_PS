from collections import deque
n, m = map(int, input().split()) # 세로 크기(높이), 가로 크기
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 상하좌우 세팅
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    count = 1

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
                count = count + 1


    return count

ans = []
art = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            art = art + 1
            ans.append(BFS(y, x))


print(art)
if art == 0:
    print(0)
else:
    print(max(ans))
