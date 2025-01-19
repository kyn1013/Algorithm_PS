def solution(s):
    words = s.split(' ')
    answer = ""
    
    for i in range(len(words)):
        word = words[i]
        for j in range(len(word)):
            if j == 0 or j % 2 == 0:
                answer += word[j].upper()
            else:
                answer += word[j].lower()
        answer += " "
        
    return answer[0:-1]
