ansList = []
while True:
    st = input()
    if st == '.':
        break
    n = []
    ans = 'yes'
    for i in st[:-1]:
        if i == '(' or i == '[':
            n.append(i)

        if len(n) > 0:
            if (i == ')' and n.pop() != '(') or (i == ']' and n.pop() != '['):
                ans = 'no'
                break
        elif len(n) == 0 and i == ']' or i == ')':
            ans = 'no'
            break
    
    if len(n) != 0: #스택이 비어있지 않은 경우
        ans = 'no'
    ansList.append(ans)

print('\n'.join(ansList))
