from collections import deque
f, s, g, u, d = map(int, input().split()) # 건물의 총 수, 현재 위치, 회사 위치, 위로 u층, 아래로 d층

distance = [0] * (f + 1)
visited = [False] * (f + 1)

def BFS(s):
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        current = queue.popleft()

        if current == g:
            return distance[current]

        for next in (current + u, current - d):
            if 0 < next <= f and not visited[next]:
                queue.append(next)
                visited[next] = True
                distance[next] = distance[current] + 1

    return "use the stairs"

print(BFS(s))
