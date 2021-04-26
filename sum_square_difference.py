square_sum = 0
sum_square = 0

for number in range(1, 101):
    square_sum += (number ** 2)

for number in range(1, 101):
    sum_square += number

sum_square = sum_square ** 2

difference = sum_square - square_sum
print(difference)