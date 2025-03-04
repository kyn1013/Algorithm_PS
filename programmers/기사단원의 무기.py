def solution(number, limit, power):
    ans = 0
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if cnt > limit:
                break
            if i % j == 0:
                cnt = cnt + 1
                if j != i // j:
                    cnt = cnt + 1
        
        if cnt > limit:
            ans = ans + power
        else:
            ans = ans + cnt
    return ans
