from collections import deque

def BFS(graph, start, n):
    queue = deque()
    queue.append(start)
    visited = [False] * (n + 1)
    distance = [0] * (n + 1) # [0, 0, 0, 0, 0, ...], 해당 노드 기준으로 나머지 노드까지의 최단 거리, distance = [0, 0, 1, 2, 1]
    visited[start] = True # "1번 노드 기준으로 각 노드까지의 최단거리"

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] is False:
                queue.append(neighbor)
                distance[neighbor] = distance[current] + 1
                visited[neighbor] = True

    return sum(distance[1:])

n, m = map(int, input().split()) # 정점의 수, 간선의 수
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

ans = []
min_score = float('inf') # 가장 무한대로 큰 수
for i in range(1, n + 1):
    score = BFS(graph, i, n)
    if score < min_score:
        min_score = score
        ans = [i]
    elif score == min_score:
        ans.append(i)

ans.sort()
print(ans[0])
