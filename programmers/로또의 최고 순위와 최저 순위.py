def solution(lottos, win_nums):
    answer = []
    min_match = 0
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    idx = 0
    lottos.sort(reverse = True)
    win_nums.sort(reverse = True)
    for i in lottos:
        if i == 0:
            break
        for j in win_nums:
            if i == j:
                min_match = min_match + 1
        idx = idx + 1
    
    max_match = min_match + len(lottos) - idx
    
    answer.append(rank[max_match])
    answer.append(rank[min_match])
    return answer
