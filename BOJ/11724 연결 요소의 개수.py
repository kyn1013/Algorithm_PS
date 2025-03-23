def DFS(graph, start, visited):
    visited[start]= True
    # print(start, end=' ')
    for i in graph[start]:
        if visited[i] is False:
            visited[i] = True
            DFS(graph, i, visited)

n, m = map(int, input().split()) # 정점, 간선의 개수

con = []
for i in range(m):
    a, b = map(int, input().split())
    con.append((a,b))

# 그래프 세팅, 이차원 리스트로 만들기
graph = []
for i in range(0, n + 1):
    graph.append([])

for a, b in con:
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
# print(graph)
ans = 0

# visited에서 0을 제외한 나머지 인덱스의 값이 true가 될 때까지 반복
for i in range(1, n + 1):
    if visited[i] is False:
        ans = ans + 1
        DFS(graph, i, visited)

# print(visited)
print(ans)
