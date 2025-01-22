n = int(input())
m = int(input())
# 1. 연결 정보에 대해 입력 받기
con = []
for _ in range(m):
    a, b = map(int, input().split())
    con.append((a, b))

# con = [[1, 2], [2, 3], [3, 5] ....]
def count(n, con):
    # 2. 방문 여부를 확인하는 리스트 생성
    visited = [False] * (n+1)
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    # 결과 : {1: [], 2: [], 3: [], 4: [], 5: []}
    # 3. 연결 정보 -> 그래프로 표현 (양방향 연결)
    for a, b in con:
        graph[a].append(b)
        graph[b].append(a)

    def DFS(node):
        # 방문한 노드는 true로 표시
        visited[node] = True
        count = 1 # 방문한 노드는 감염되었기에 숫자 1증가
        for n in graph[node]:
            if not visited[n]:
                count += DFS(n) #방문한 노드의 이웃 노드가 탐색을 안한 곳이라면 그곳을 또 탐색
        return count

    result = DFS(1)
    return result -1

print(count(n, con))
