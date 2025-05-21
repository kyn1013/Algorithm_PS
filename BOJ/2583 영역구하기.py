from collections import deque
m, n, k = map(int, input().split()) # m = 높이, n = 가로 길이

# 그래프 세팅
graph = []
for _ in range(m):
    row = []
    for _ in range(n):
        row.append(0)
    graph.append(row)

# 입력받은 정사각형 좌표들을 1로 마킹
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

# 상하좌우 세팅
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0인 부분만 그래프 탐색 시작
def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    # 얘도 방문했기 때문에 1로 변경해줘야 함
    graph[y][x] = 1
    count = 1

    while queue:
        y1, x1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[ny][nx] == 1:
                continue
            if graph[ny][nx] == 0:
                queue.append((ny, nx))
                graph[ny][nx] = 1
                count = count + 1

    return count

distance = []
ans = 0

for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            ans = ans + 1
            distance.append(BFS(y, x))

distance.sort()
print(ans)
for i in distance:
    print(i, end=" ")
