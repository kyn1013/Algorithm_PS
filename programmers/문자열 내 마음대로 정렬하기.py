def solution(strings, n):
    answer = []
    num = []
    #정렬 인덱스를 뽑은 리스트 만들기
    for i in strings:
        num.append([i[n], i])
    num.sort(key = lambda m : (m[0], m[1]))
    for i in num:
        answer.append(i[1])
    return answer
