s = list()

msg = input("문자열 입력 : ")
for c in msg :
    s.append(c)

print("문자열 출력 : ", end='')
while len(s) > 0:
    print(s.pop(), end='')
print()
