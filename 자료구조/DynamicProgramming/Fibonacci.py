#메모이제이션 - 한번 계산한 값을 저장해놨다가 재활용
def fib_dp_mem(n):
    if(mem[n] == None):
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

#테이블화 - 부분 문제의 해를 메모리에 저장하고, 테이블 항목을 순서대로 상향식으로 채워나감
def fib_dp_tab(n):
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n] #결과반환

n = 8
mem = [None] * (n+1)
print('Fibonacci(%d) 테이블화 = '%n, fib_dp_tab(n))
print('Fibonacci(%d) 메모이제이션 = '%n, fib_dp_mem(n))
