def solution(food):
    ans = ""
    half = []
    idx = 1

    for i in food[1:]:
        half.append(i//2)

    for i in half:
        for j in range(i):
            ans += str(idx)
        idx = idx + 1

    ans += str(0)

    idx = idx - 1
    for i in half[::-1]:
        for j in range(i):
            ans += str(idx)
        idx = idx - 1
        
    return ans
