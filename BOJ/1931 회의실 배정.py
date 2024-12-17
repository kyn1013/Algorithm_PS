n = int(input())
meeting = []
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

#회의 시간이 먼저 끝나는 순으로 정렬, 회의 시간이 동시에 끝난다면 시작 시간이 빠른 순으로 정렬
meeting.sort(key=lambda x : (x[1], x[0]))

count = 0
end_time = 0

#그리디 알고리즘으로 계산
#시작 시간이 이전에 진행한 회의의 종료 시간 이후라면 선택
for start, end in meeting:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
