def solution(n):
    answer = 0
    three_number = ""
    while n > 0:
        three_number += str(n % 3)
        n //= 3
        
    answer = int(three_number, 3)
    return answer
