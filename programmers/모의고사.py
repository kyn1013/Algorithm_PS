def solution(answers):
    sol1 = [1, 2, 3, 4, 5]
    sol2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sol3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    idx1 = 0
    idx2 = 0
    idx3 = 0

    cnt = {1:0, 2:0, 3:0}

    for i in answers:

        if i == sol1[idx1 % len(sol1)]:
            cnt[1] = cnt[1] + 1
        idx1 = idx1 + 1

        if i == sol2[idx2 % len(sol2)]:
            cnt[2] = cnt[2] + 1
        idx2 = idx2 + 1

        if i == sol3[idx3 % len(sol3)]:
            cnt[3] = cnt[3] + 1
        idx3 = idx3 + 1

    max_val = max(cnt.values())
    ans = []
    for i in cnt:
        if cnt[i] == max_val:
            ans.append(i)

    ans.sort()
    return ans
