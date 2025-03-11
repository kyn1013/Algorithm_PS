def solution(babbling):
    ans = 0
    word = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for w in word:
            if w * 2 not in i:
                i = i.replace(w," ")
        
        if i.strip() == "":
            ans = ans + 1
        
    return ans
