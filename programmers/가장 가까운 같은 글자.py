def solution(s):
    ans = []
    dic = {}
    idx = 0
    #문자열 처음부터 순환
    for i in s:
    #문자열이 딕셔너리에 없는 경우
        if i not in dic.keys():
            dic[i] = idx
            ans.append(-1)
            idx += 1
    #문자열이 딕셔너리에 있는 경우
        else:
            ans.append(idx - dic[i])
            dic[i] = idx
            idx += 1
    return ans
