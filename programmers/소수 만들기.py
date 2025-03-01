import itertools
def solution(nums):
    answer = 0
    num = list(itertools.combinations(nums, 3))
    for i in num:
        isPrime = 0
        k = sum(i)
        for j in range(2, k):
            if k % j == 0:
                isPrime = 1
                break
        if isPrime == 0:
            answer = answer + 1
    return answer
