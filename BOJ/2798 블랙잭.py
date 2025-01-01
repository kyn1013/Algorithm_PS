n, m = map(int, input().split()) #카드의 개수 / 가장 가까워야 하는 수
cards = list(map(int, input().split())) #카드 리스트
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = cards[i] + cards[j] + cards[k]
            if m >= card_sum and card_sum > result:
                result = card_sum

print(result)
