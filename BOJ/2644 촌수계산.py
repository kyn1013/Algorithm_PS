from collections import deque

def BFS (graph, start, n, goal):
    queue = deque()
    queue.append(start)
    visited = [False] * (n + 1)
    visited[start] = True
    distance = [0] * (n + 1)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] is False:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
                visited[neighbor] = True

                if neighbor == goal:
                    return distance[neighbor]

    return -1

n = int(input()) # 전체 사람의 수 (노드 수)
x, y = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) # 부모, 자식간의 관계의 수 (간선 수)
con = []
for _ in range(m):
    a, b = map(int, input().split())
    con.append((a, b))

graph = []
for _ in range(n + 1):
    graph.append([])

for a, b in con:
    graph[a].append(b)
    graph[b].append(a)

print(BFS(graph, x, n, y))


