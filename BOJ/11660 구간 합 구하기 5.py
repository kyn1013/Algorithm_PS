n, s = map(int, input().split()) #배열크기, 입력받을 횟수

numberList = [] #2차원 배열
for _ in range(n):
    a = list(map(int, input().split()))
    numberList.append(a)

sumList = [[0]*(n+1) for _ in range(n+1)] #합배열 만들기

for i in range(1, n+1):
    for j in range(1, n+1):
        sumList[i][j] = numberList[i-1][j-1] + sumList[i-1][j] + sumList[i][j-1] - sumList[i-1][j-1]

ans =[]
for i in range(s):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sumList[x2][y2] - sumList[x1-1][y2] - sumList[x2][y1-1] + sumList[x1-1][y1-1]
    ans.append(str(answer))

print("\n".join(ans))
