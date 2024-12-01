def Knapsack01_BF(wgt, val, W):
    n = len(wgt) #전체 물건의 수
    bestVal = 0 #배낭의 최대 가치
    bestLst = []

    for i in range(2**n): #부분집합의 수는 2의 n제곱
        s = [0]*n
        temp = i
        for d in range(n): #i를 이진수로 변환했을 때 각 자리의 수를 리스트에 저장
            s[d] = temp%2
            temp = temp//2

        #현재 경우에 대한 물건의 총 무게와 총 가치를 구함
        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1:
                sumWgt += wgt[d]
                sumVal += val[d]
        # 디버깅 출력 추가
        print(f"i = {i}, 부분집합: {s}, 무게합: {sumWgt}, 가치합: {sumVal}")

        #가능한 부분 집합이고 가치합이 최대 가치보다 크면 가치 갱신
        if sumWgt <= W:
            if sumVal > bestVal:
                bestVal = sumVal
                bestLst = list(s)

    print("최적 물건 선택 (이진수 형태):", bestLst)
    return bestVal #최대 가치 반환



weight = [10, 20, 30, 25, 35]	# 물건별 무게
value  = [60, 100, 120, 70, 85]	# 물건별 가치
W = 80				            # 배낭의 제한 용량

print("Knapsack01-BruteForce:", Knapsack01_BF(weight, value, W))
