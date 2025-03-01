import itertools
def solution(nums):
    answer = 0
    num = list(itertools.combinations(nums, 3))
    for i in num:
        isPrime = 0
        for j in range(2, sum(i)):
            if sum(i) % j == 0:
                isPrime = 1
        if isPrime == 0:
            answer = answer + 1
    return answer
