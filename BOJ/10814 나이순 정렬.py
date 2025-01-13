n = int(input())
members = []
sequence = 1
for _ in range(n):
    age, name = input().split()
    members.append([int(age), name, sequence])
    sequence += 1

members.sort(key = lambda m : (m[0], m[2]))

for i in members:
    print(str(i[0]) + " " + str(i[1]))

