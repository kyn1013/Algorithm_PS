n = int(input())
score = list(map(int, input().split()))
score.sort(reverse=True) #내림차순으로 정렬
sum = 0
for i in score:
    sum += i / score[0] * 100

print(sum/n)
