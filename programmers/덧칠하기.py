def solution(n, m, section):
    ans = 1
    start = section[0] #페인트 칠하는 시작점
    for i in range(1, len(section)):
        if start + m - 1 < section[i]:
            ans = ans + 1
            start = section[i]
    return ans
