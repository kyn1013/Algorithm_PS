INF = 999
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if selected[v]==False and dist[v]<mindist: #MST에 포함되지 않은 정점 중에서 최소 dist를 갖는 정점의 인덱스 minv를 구함
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj): #인접행렬, 정점리스트
    n = len(vertex)
    dist = [INF] * n
    dist[0] = 0
    selected = [False] * n

    for _ in range(n): #n개의 정점을 MST에 추가하면 종료됨
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')
        for v in range(n): #간선 (u, v)가 있고 v가 MST에 포함하지 않으면

            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

        print(': ', dist)

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [0,	   25,		INF,	12,	  INF,     INF,		INF],
           [25,		0,	    10,		INF,	15,	   INF,	    INF],
           [INF,	10,		0,	    INF,	INF,	INF,	16],
           [12,	    INF,    INF,	0,      17,	    37,	    INF],
           [INF,	15,	    INF,    17,	    0,      19,		14  ],
           [INF,	INF,	INF,	37,     19,		0,	    42],
           [INF,    INF,	16,     INF,	14,		42,	    0   ]]

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)
