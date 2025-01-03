n = int(input()) # 사람 수
humans = [] # 덩치가 담긴 리스트
ranking = [] # 순위가 담긴 리스트
for i in range(n):
    x, y = map(int, input().split())
    humans.append([x, y])

for i in range(n):
    count = 1
    for h in humans:
        if h[0] > humans[i][0] and h[1] > humans[i][1]:
            count += 1
    ranking.append(count)

for i in ranking:
    print(i, end=" ")
