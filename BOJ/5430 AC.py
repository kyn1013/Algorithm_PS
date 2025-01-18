import collections
t = int(input())
ans = []

for _ in range(t):
    ac = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    deq = collections.deque(arr)

    flag = 0 # 뒤집은 상태인지 아닌지 확인하는 변수, 홀수면 뒤집은 것
    err_count = False

    if n == 0: # 길이가 0이라면 빈 덱으로 초기화
        deq = []

    for i in ac:
        if i == "R":
            flag += 1

        if i == "D":
            if len(deq) == 0:
                ans.append("error")
                err_count = True
                break
            else:
                if flag % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()

    if not err_count:
        if flag % 2 == 0:
            result = "[" + ",".join(map(str, deq)) + "]"
            ans.append(result)
        else:
            deq.reverse()
            result = "[" + ",".join(map(str, deq)) + "]"
            ans.append(result)

for i in ans:
    print(i)
