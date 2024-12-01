def KnapSackFrac(wgt, val, W): #무게, 가치, 최대 용량 (물건들은 단위 무게당 가격의 내림차순으로 정렬되어 있어야 함)
    bestVal = 0
    for i in range(len(wgt)):
        if W <= 0:
            break
        if W >= wgt[i]:
            W -= wgt[i]
            bestVal += val[i]
        else:
            fraction = W / wgt[i]
            bestVal += val[i] * fraction
            break

    return bestVal #최대 가치 반환

weight = [12, 10, 8]
value = [120, 80, 60]
W = 18
print(KnapSackFrac(weight, value, W))
