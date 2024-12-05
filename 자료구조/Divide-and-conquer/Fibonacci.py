def powerMat(x, n) :
    if n == 1 :												# 종료조건
        return x
    elif (n % 2) == 0 :                     				# n이 짝수
        return powerMat(multMat(x,x), n // 2)
    else :													# n이 홀수
        return multMat(x, powerMat(multMat(x,x), (n - 1) // 2))

def multMat(A, B) :
    rows = len(A) #행
    cols = len(B[0]) #열
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

#분할 정복은 같은 부분 문제가 여러 번 반복되어 나타나지 않을 때 사용해야 함 -> 시간복잡도 2의 n제곱
def fib(n):
    if n == 0: return 0 #정복: 0번째 달
    elif n == 1: return 1 #정복: 1번쨰 달
    else:
        return fib(n-1) + fib(n-2)

def fib_mat(n):
    if n == 0: return 0 #정복: 0번째 달
    elif n == 1: return 1 #정복: 1번쨰 달

    mat = [[1,1], [1,0]] #초기 피보나치 행렬
    result = powerMat(mat, n) #축소정복 방식
    return result[0][1] #fib(n) 부분을 반환
