def DFS(g, start, visited):
    visited[start] = True

    for i in g[start]:
        if visited[i] is False:
            DFS(g, i, visited)

t = int(input())
ans_arr = []

for i in range(t):

    n = int(input())
    graph = []
    for _ in range(n + 1):
        graph.append([])

    v = list(map(int, input().split()))
    for i in range(1, n + 1):
        graph[i].append(v[i - 1])

    visited = [False] * (n + 1)
    ans = 0

    for i in range(1, n + 1):
        if visited[i] is False:
            DFS(graph, i, visited)
            ans = ans + 1

    ans_arr.append(ans)

for i in ans_arr:
    print(i)
