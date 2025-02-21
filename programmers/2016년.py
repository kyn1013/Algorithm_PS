def solution(a, b):
    # 2016년 각 월의 일 수
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    # 2016년 1월 1일은 금요일 (FRI)
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 1월 1일은 금요일, 1월 1일을 입력했다면 1월 1일로부터 경과일은 0일임
    elapsed_date = sum(month[:a]) + b - 1
    
    return week[elapsed_date % 7]
