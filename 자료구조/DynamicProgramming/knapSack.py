#분할정복
def knapSack_df(W, wt, val, n): #배낭 용량, 무게, 가치, 물건의 수
    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W): #마지막 물건을 넣을 용량이 부족한 경우, 이 물건을 제외한 최대가치를 구함
        return knapSack_df(W, wt, val, n-1)
    else:
        valWithout = knapSack_df(W, wt, val, n-1)
        valWith = val[n-1] + knapSack_df(W-wt[n-1], wt, val, n-1)
        return max(valWith, valWithout) #둘 중에서 더 큰 값

#동적계획법
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n+1)]

    for i in range(1, n+1): #위에서 아래로 진행
        for w in range(1, W+1): #좌에서 우로 진행
            if wt[i - 1] > w: #i번째 물건이 용량 초과
                A[i][w] = A[i-1][w]
            else: #i번째 물건을 넣을 수 있음
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][w]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print("0-1배낭문제(분할 정복): ", knapSack_df(W, wt, val, n))
print("0-1배낭문제(동적 계획): ", knapSack_dp(W, wt, val, n))
