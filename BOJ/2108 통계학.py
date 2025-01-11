n = int(input())

number_list = []
for _ in range(n):
    k = int(input())
    number_list.append(k)

f = {} #최빈값을 저장할 딕셔너리
for n in number_list:
    if n in f: #키값이 이미 딕셔너리에 존재한다면, 기존에 있는 거에서 1증가
        f[n] += 1
    else:
        f[n] = 1

max_count = max(f.values()) #가장 많이 나온 빈도수
modes = []
m_result = 0

for key, value in f.items():
    if value == max_count:
        modes.append(key)


if len(modes) == 1:
    m_result = modes[0]
else:
    modes.sort()
    m_result = modes[1]


avg = round(sum(number_list) / len(number_list))
number_list.sort()
median = number_list[len(number_list) // 2]

number_range = max(number_list) - min(number_list)

print(avg)
print(median)
print(m_result)
print(number_range)



