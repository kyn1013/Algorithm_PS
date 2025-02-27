def solution(k, m, score):
    score.sort() # 오름차순 정렬
    ans = 0

    while len(score) >= m:
        s = score[-m:]
        del score[-m:]
        ans = ans + s[0] * m
    return ans
