def solution(cards1, cards2, goal):
    answer = "Yes"
    while(len(cards1) or len(cards2)):
        if len(goal) == 0:
            break
        elif len(cards1) > 0 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif len(cards2) > 0 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
        else:
            answer = "No"
            break
            
    return answer
