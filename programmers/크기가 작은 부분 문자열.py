import collections

def solution(t, p):
    answer = 0
    t_len = len(t)
    p_len = len(p)
    start = 0
    end = p_len

    while t_len - p_len >= 0:
        n = int(t[start:end])
        if n <= int(p):
            answer += 1
        start += 1
        end += 1
        t_len -= 1

    return answer

