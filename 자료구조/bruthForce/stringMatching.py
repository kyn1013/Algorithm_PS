def string_matching(T, P): #입력문자열, 탐색패턴
    n = len(T) #텍스트의 길이
    m = len(P) #패턴의 길이

    for i in range(n-m+1):
        j = 0
        while j < m and P[j] == T[i+j]: #현재 텍스트 위치에서 패턴의 첫 문자부터 하나씩 텍스트 문자와 비교
            j = j + 1
        if j == m: #맨끝까지 일치하면 매칭 성공, 현재 위치 i 반환
            return i #매칭 성공
    return -1 #매칭 실패
