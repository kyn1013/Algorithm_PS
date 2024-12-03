def slow_power(x, n): #반복으로 x의 n제곱을 구하는 함수
    result = 1.0
    for i in range(n):
        result = result * x
    return result

def power(x, n):
    if n == 1: #1 제곱인 경우
        return x
    elif (n % 2) == 0: #짝수 제곱인 경우
        return power(x*x, n//2)
    else: #홀수 제곱인 경우
        return x * power(x*x, (n-1)//2)


import time		# time 모듈 포함
print("    억지기법(2**500) =", power(2.0, 500))
print("축소정복기법(2**500) =", slow_power(2.0, 500))

t1 = time.time()
for i in range(100000) : power(2.0, 500)			# 축소정복 10만회
t2 = time.time()
for i in range(100000) : slow_power(2.0, 500)	# 억지기법 10만회
t3 = time.time()

print("    억지기법 시간... ", t3-t2)
print("축소정복기법 시간... ", t2-t1)
