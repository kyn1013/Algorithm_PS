def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True

    for v in range(len(vtx)): #방문하지 않은 이웃 정점 v가 있으면 그 정점을 시작으로 다시 DFS 호출
        if adj[s][v] != 0:
            if visited[v]==False:
                DFS(vtx, adj, v, visited)

def ST_DFS(vtx, adj, s, visited): #신장트리
    visited[s] = True

    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v]==False:
                print("(", vtx[s], vtx[v], ")", end=' ')
                DFS(vtx, adj, v, visited)

vtx = ['U','V','W','X','Y']
edge= [[0,  1,  1,  0,  0],
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()

