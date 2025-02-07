def solution(numbers):
    answer = []
    num = list(numbers)
    for i in range(0, len(num)):
        for j in range(i+1, len(num)):
            answer.append(num[i]+num[j])
    answer.sort()
    set_answer = set(answer)
    answer = list(set_answer)
    answer.sort()
    return answer
