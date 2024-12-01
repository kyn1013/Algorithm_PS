def check(n):
    for i in range(n):
        sum = 0
        k = str(i)
        for j in k:
            sum += int(j)
        sum += i
        if sum == n:
            return k

    return 0

n = int(input())
print(check(n))
