n = int(input()) #도시의 개수
distence = list(map(int, input().split())) #도시간의 거리
city = list(map(int, input().split())) #각 도시별 주유 비용

cost = 0
min_cost = city[0]

for i in range(n-1): #거리 갯수만큼 반복
    
    #현재 최소 비용보다 더 작다면 갱신
    if min_cost > city[i]:
        min_cost = city[i]

    cost += min_cost * distence[i]

print(cost)
