def check(str):
    stack = list()
    for i in str:
        if (i == '(') :
            stack.append(i)
        else :
            if (len(stack) == 0) :
                return "NO"
            else :
                left = stack.pop()
                if(left == '(' and i != ')') :
                    return "NO"
    if (len(stack) == 0) :
        return "YES"
    else :
        return "NO"

count = int(input())
ans = []

for i in range(0,count):
    st = input()
    ans.append(check(st))

for i in ans:
    print(i, end='')
    print()
