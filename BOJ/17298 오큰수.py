n = int(input())
number = list(map(int, input().split()))
ans = [-1] * n #정답 리스트 초기화
stack = []

for i in range(n-1, -1, -1): #역순으로 조회 (자신보다 큰 수 중에 가장 오른쪽에 있는 수이므로)

    while stack and stack[-1] <= number[i]: #자신보다 작거나 같은 수는 제거
        stack.pop()

    if stack: #자신보다 큰 수중에 가장 최근에 들어온 수(더 오른쪽에 있는 수)를 오큰수로 지정
        ans[i] = stack[-1]

    stack.append(number[i])

for i in ans:
    print(i, end=' ')

