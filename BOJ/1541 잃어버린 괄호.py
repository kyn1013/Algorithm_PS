n = input().split('-') #-를 기준으로 리스트로 나눔 / 2 + 3 + 5 - 1 + 7 - 8

#n[0] = 2 + 3 + 5
ans = sum(map(int, n[0].split('+'))) #-이전의 값은 +를 기준으로 나눠서 더함

#- 이후의 다 더할 값들 순회 후 빼기
for i in n[1:]:
    ans -= sum(map(int, i.split('+')))

print(ans)
