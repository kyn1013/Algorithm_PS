number1, number2 = map(int, (input().split()))

end = max(number1, number2)
max_number = 0
for i in range(1, end+1):
    if number1 % i == 0 and number2 % i == 0:
        max_number = i

min_number = (number1 // max_number) * (number2 // max_number) * max_number
print(max_number)
print(min_number)
