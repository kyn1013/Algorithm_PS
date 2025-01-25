def solution(n, m):
    answer = []
    max_num = 0
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            max_num = i
        

    a = n / max_num
    b = m / max_num
    
    min_num = a * b * max_num   
    answer.append(max_num)
    answer.append(min_num)
    return answer
