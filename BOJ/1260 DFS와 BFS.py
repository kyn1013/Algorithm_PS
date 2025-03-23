from collections import deque
def DFS(graph, start, visited, dfs_ans):
    visited[start] = True
    dfs_ans.append(start)

    for i in graph[start]:
        if visited[i] is False:
            DFS(graph, i, visited, dfs_ans)

def BFS(graph, start, visited, bfs_ans):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        bfs_ans.append(v)
        for i in graph[v]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
con = []
for _ in range(m):
    a, b = map(int, input().split())
    con.append((a, b))

graph = []
for i in range(n+1):
    graph.append([])

for a, b in con:
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
dfs_ans = []
bfs_ans = []

DFS(graph, v, dfs_visited, dfs_ans)
BFS(graph, v, bfs_visited, bfs_ans)

for i in dfs_ans:
    print(i, end=" ")

print()
for i in bfs_ans:
    print(i, end=" ")
