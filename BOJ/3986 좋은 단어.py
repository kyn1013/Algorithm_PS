count = int(input())
ans = 0
for _ in range(count):
    n = input()
    st = []
    for i in n:
        if len(st) == 0 or st[-1] != i:
            st.append(i)
        elif st[-1] == i: #스택에서 같은 값을 만나면
            st.pop()

    if len(st) == 0:
        ans += 1

print(ans)
