from collections import deque
n, k = map(int, input().split())

def BFS(n, k):
    max_value = 100001
    visited = [False] * max_value
    distance = [0] * max_value
    queue = deque()
    queue.append(n)
    visited[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            return distance[current]

        for next in (current - 1, current + 1, current * 2):
            if next >= 0 and next < max_value and not visited[next]:
                queue.append(next)
                visited[next] = True
                distance[next] = distance[current] + 1

print(BFS(n, k))
