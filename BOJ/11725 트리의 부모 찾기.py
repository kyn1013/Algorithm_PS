import collections
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1) #부모 정보 저장할 리스트

def bfs():
    queue = collections.deque([1]) #첫번째 요소로 1이 들어간 덱 생성

    while queue: #덱이 비어있지 않을 때까지 반복
        current_node = queue.popleft()

        for neighbor in graph[current_node]:
            if parent[neighbor] == 0: #부모가 없으면
                parent[neighbor] = current_node #현재 노드를 부모 노드로 추가
                queue.append(neighbor)


bfs()

for i in range(2, n+1):
    print(parent[i])

