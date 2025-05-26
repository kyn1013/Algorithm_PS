n, m = map(int, input().split()) # 달걀의 개수, 손님의 수
consumer = [] # 각 손님별로 구매할 수 있는 가격의 최대값
for _ in range(m):
    price = int(input())
    consumer.append(price)

consumer.sort()
idx = 0
ans_price = 0
ans_egg_price = 0
for p in consumer:
    count = min(n, len(consumer[idx:]))
    idx = idx + 1
    max_price = count * p
    if ans_price < max_price:
        ans_price = max_price
        ans_egg_price = p

print(ans_egg_price, ans_price)
