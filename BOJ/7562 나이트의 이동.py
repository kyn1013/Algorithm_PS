from collections import deque
case = int(input())
ans = []
for _ in range(case):
    n = int(input())
    graph = []
    for _ in range(n):
        row = [0] * n
        graph.append(row)

    distance = []
    for _ in range(n):
        row = [0] * n
        distance.append(row)

    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    # 시계방향대로 이동 할 수 있는 수를 둠, BFS에서는 방향 순서를 신경써야 함
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def BFS(y, x):
        queue = deque()
        queue.append((y, x))
        graph[y][x] = 1

        while queue:
            y, x = queue.popleft()

            if y == goal_y and x == goal_x:
                return distance[y][x]

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
                    distance[ny][nx] = distance[y][x] + 1
                    queue.append((ny, nx))
                    graph[ny][nx] = 1

    ans.append(BFS(start_y, start_x))

for i in ans:
    print(i)
