def solution(k, score):
    best = score[:k]
    m = []
    ans = []
    new_score = score[k:]
    # 프로그램 시작 이후 초기 k일
    for i in best:
        m.append(i)
        m.sort(reverse=True) # 내림차순 정렬
        ans.append(m[-1])

    # k일 이후
    for i in new_score:
        best.sort(reverse=True) # 내림차순 정렬 100.10,1 ...
        if best[-1] < i:
            best.pop()
            best.append(i)
            best.sort(reverse=True)
            ans.append(best[-1])
        else:
            ans.append(best[-1])
    
    return ans
