n = int(input())
book = {}

for _ in range(n):
    title = input()

    # 이미 딕셔너리에 값이 있다면 1 증가, 아니라면 값 1 넣기
    if title in book:
        book[title] = book[title] + 1
    else:
        book[title] = 1

# 딕셔너리의 값들 중, 가장 큰 수 추출
best = max(book.values())

ans = []
# 딕셔너리를 탐색하며 가장 큰 수와 같은 값을 가진 책 이름 리스트에 추가
for key, value in book.items():
    if value == best:
        ans.append(key)
# 오름차순으로 알파벳 정렬
a = sorted(ans)
print(a[0])
