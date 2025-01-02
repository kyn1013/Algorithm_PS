n = int(input())
ans = 0
for i in range(n):
    num = i #자기 자신 더하기
    current_num = i
    while current_num > 0:
        num += current_num % 10 #자릿수마다 더하기
        current_num //= 10 #더한 자릿수는 제거

    if num == n:
        ans = i
        break

print(ans)
