n, count = map(int, input().split()) #수, 입력받을 횟수
num = list(map(int, input().split())) #배열
sumArr = [0] * n #합배열
ans = []

sumArr[0] = num[0]

for i in range(1, n):
    sumArr[i] = sumArr[i - 1] + num[i]


for _ in range(count):
    start, end = map(int, input().split())

    if start == 1:
        ans.append(sumArr[end-1])

    else:
        ans.append(sumArr[end-1] - sumArr[start-2])

for i in ans:
    print(i)
