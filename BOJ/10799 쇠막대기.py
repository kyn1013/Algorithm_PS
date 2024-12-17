n = input()

stack = []
count = 0
for i in range(len(n)):

    #"(" 라면 스택에 추가
    if n[i] == "(":
        stack.append(n)

    #")" 라면 스택에서 쌍을 이루는 "("를 제거 후, stack의 길이만큼 조각 추가
    else:
        stack.pop()
        #바로 앞의 값이 "("라면 문자열의 끝이 아니므로 길이만큼 추가
        if n[i-1] == "(":
            count += len(stack)
        #문자열의 끝
        else:
            count += 1

print(count)
