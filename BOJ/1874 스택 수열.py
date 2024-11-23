def stack(request):
    current = 1
    result = []
    st = []

    for i in request:
        while current <= i:
            st.append(current)
            result.append('+')
            current += 1

        if st[-1] == i:
            st.pop()
            result.append('-')
        else:
            return ['NO']

    return result


n = int(input())
request = []
for _ in range(n):
    request.append(int(input()))
ans = stack(request)
print("\n".join(ans))

